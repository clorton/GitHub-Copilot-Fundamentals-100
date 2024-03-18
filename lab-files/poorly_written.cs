using System;

class Program
{
    const int MAX = 100;

    static int Sum(int[] arr)
    {
        int result = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            result += arr[i];
        }
        return result;
    }

    static int ReadIntFromConsole(string prompt, int min, int max)
    {
        int result;
        do
        {
            Console.Write(prompt);
        } while (!int.TryParse(Console.ReadLine(), out result) || result < min || result > max);
        return result;
    }

    static void Main()
    {
        int n = ReadIntFromConsole("Enter the number of elements (1-100): ", 1, MAX);

        int[] arr = new int[n];

        Console.WriteLine($"Enter {n} integers:");
        for (int i = 0; i < n; i++)
        {
            arr[i] = ReadIntFromConsole($"Enter integer {i+1}: ", int.MinValue, int.MaxValue);
        }

        int total = Sum(arr);

        Console.WriteLine($"Sum of the numbers: {total}");
    }
}
