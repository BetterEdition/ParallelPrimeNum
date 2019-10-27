using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Collections.Concurrent;

namespace ParallelProgram
{
    class Program
    {
        static List<int> ints = new List<int> { 3, 7, 5, 45, 3245763, 32436576, 3443134, 35765634, 2456345, 34232 };
        private static CancellationTokenSource source = new CancellationTokenSource();
        static void Main(string[] args)
        {
            samplePipeline();
            /*try
            {
                var t1 = Task.Factory.StartNew(() => DoSomething(1, 1500, source.Token)).ContinueWith((prevTask) => DoSomethingElse(1, 1000));
                Task.WaitAny(t1);
                Task.Factory.StartNew(() => DoSomething(2, 3000, source.Token)).ContinueWith((prevTask) => DoSomethingElse(2, 3000));
                Task.Factory.StartNew(() => DoSomething(3, 1000, source.Token)).ContinueWith((prevTask) => DoSomethingElse(3, 4000));

               
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.GetType());
            }
            
                    
                    

                    var intList = new List<int> {1,2,3,4,434,3243,4,124,13,23,132,312,31,2312,31,31,23};
*/
            /*Stopwatch stopWatch = new Stopwatch();
            stopWatch.Start();

            ParallelAggregateWithPLinq();
            ParallelAggregateExample();

            stopWatch.Stop();

            TimeSpan ts = stopWatch.Elapsed;

            // Format and display the TimeSpan value.
            string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
                ts.Hours, ts.Minutes, ts.Seconds,
                ts.Milliseconds / 10);
            Console.WriteLine("RunTime " + elapsedTime);
            */
            Console.ReadLine();
        }

        static void samplePipeline()
        {

            var bc = new BlockingCollection<int>();
            var bc2 = new BlockingCollection<int>();
            var factory = new TaskFactory();

            var firstTask = factory.StartNew(() => FindNumberToSquare(bc));
            var secondTask = factory.StartNew(() => CalcSquareNumber(bc, bc2));
            var thirdTask = factory.StartNew(() => ShowSquaredNumber(bc2));

            Task.WaitAll(firstTask, secondTask, thirdTask);

        }

        static void FindNumberToSquare(BlockingCollection<int> bc)
        {
            bc.Add(5);
            bc.CompleteAdding();

        }

        static void CalcSquareNumber(BlockingCollection<int> bc, BlockingCollection<int> bc2)
        {
            int number = bc.Take();
            bc2.Add(number * number);
            bc2.CompleteAdding();

        }
        static void ShowSquaredNumber(BlockingCollection<int> bc2)
        {
            Console.WriteLine(bc2.Take());
           
        }
        static void ParallelAggregateExample()
        {
              
            object lockObject = new object();
            double sum = 0.0;

            Parallel.ForEach(ints, () => 0.0, (currentNum, loopState, partialResult) =>
            {
                
                return currentNum + partialResult;
            },
            (localPartialSum) =>
            {

                {
                    lock (lockObject)
                    {
                        sum += localPartialSum;
                    }
                }
        });
            Console.WriteLine(sum);
        }

        static void ParallelAggregateWithPLinq()
        {
            // No locking requried
           var sum2 = (from x in ints.AsParallel() select x)
                    .Aggregate(0, (y1, y2) => y1 + y2);
            Console.WriteLine("Using PLinq - Aggregate: " + sum2);
        }


        public static void SumSquares(IEnumerable<int> source)

        {
            Console.WriteLine((source.Aggregate(0, (sum, x) => sum + x * x, (sum) => sum)));
        }

        static void DoSomething(int id, int sleepTime, CancellationToken token)
        {
            
            if (token.IsCancellationRequested)
            {
                Console.WriteLine("Cancelled requested");
                token.ThrowIfCancellationRequested();
            }
            Console.WriteLine("Task {0} is beginning", id);
            Thread.Sleep(sleepTime);
            Console.WriteLine("Task {0} has completed", id);
            if(id == 1)
            {
                source.Cancel();
            }

        }
        static void DoSomethingElse(int id, int sleepTime)
        {

            Console.WriteLine("More Task {0} is beginning", id);
            Thread.Sleep(sleepTime);
            Console.WriteLine("More Task {0} has completed", id);

        }
    }
}
