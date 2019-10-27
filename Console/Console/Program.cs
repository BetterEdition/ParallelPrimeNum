using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace Consoled
{
    class Program
    {
        static void Main(string[] args)
        {
                IEnumerable<int> nums = Enumerable.Range(0, 6400000).ToList();
                long total = 0;

                // First type parameter is the type of the source elements
                // Second type parameter is the type of the thread-local variable (partition subtotal)
                Stopwatch stopwatch = new Stopwatch();
                stopwatch.Start();

                Parallel.ForEach<int, long>(nums, // source collection
                                            () => 0, // method to initialize the local variable
                                            (j, loop, subtotal) => // method invoked by the loop on each iteration
                                        {
                                                if (IsPrime(j))
                                                {
                                                    subtotal += 1; //modify local variable
                                            }

                                                return subtotal; // value to be passed to next iteration
                                        },
                                            // Method to be executed when each partition has completed.
                                            // finalResult is the final value of subtotal for a particular partition.
                                            (finalResult) => Interlocked.Add(ref total, finalResult)
                                            );
                stopwatch.Stop();

                Console.WriteLine("The total primes for range 1 -: " + nums.Count(), "{ 0:N0}", total);
                Console.WriteLine("Parallel loop time in milliseconds: {0}",
                                   stopwatch.ElapsedMilliseconds);

            }
        public static bool IsPrime(int numberToTest)
        {

            // Test whether the parameter is a prime number.
            if ((numberToTest & 1) == 0)
            {
                if (numberToTest == 2)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            // Note:
            // ... This version was changed to test the square.
            // ... Original version tested against the square root.
            // ... Also we exclude 1 at the end.
            for (int i = 3; (i * i) <= numberToTest; i += 2)
            {
                if ((numberToTest % i) == 0)
                {
                    return false;
                }
            }
            return numberToTest != 1;
        }

    }
}
