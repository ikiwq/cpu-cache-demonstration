# Examples of bad CPU cache usage.
In this project, some examples of how bad CPU usage can lead to worse performance will be described..

## Matrices Example
In the Matrices folder is presented an example of a matrices sum. 
- In the first example, both matrices are accessed in a row-major order. 
- In the second example, the first matrix is accessed in a row-major order and the second in a column-major order. This took 1.5 seconds more than the previous one.
- In the third example, both the matrices are accessed in column-major order. This took 3 times the first approach and 2 times the first approach.

#### Explanation 
This has to do with the way data is laid out and accessed.

<img src="https://github.com/ikiwq/cpu_cache_demonstration/assets/110495658/3ddadadf-d96d-4616-bd23-597578bac262" width="750"/>

Arrays are contiguous in memory. Matrices are arrays of arrays. When accessing the rows first, we are actually accessing the array one value after another. 
When accessing the column first, we are instead picking values from different arrays sequentially, effectively 
jumping between segments of memory.

When the CPU loads data into its cache, it doesn't load a single value. Instead, it usually loads a segment of memory known as a cache line.

When accessing an array, the CPU loads the array into its memory, making row-major access quick. When accessing a column, we have to take the value from another array, forcing the CPU to fetch from the main memory.

## DOD vs OOP Example
In the dod folder is presented an example of DOD patterns vs. OOP patterns.
- The first iteration creates instances of a particle class and calls a member function to update them.
- In the second iteration, the values inside the member functions are laid into two parallel arrays. A velocity_x[i] will have its corresponding position at positions_x[i].

Both iterations have similar results.

If we do a bonus iteration, but this time bloating the class with useless fields, it takes two times the initial amount of time.

#### Explaination
The way data is laid out plays a crucial role, as the example above shows.

<img src="https://github.com/ikiwq/cpu_cache_demonstration/assets/110495658/2b8249e7-7f3c-4a1d-9379-5579f6897ffa" width="750"/>

Fields in classes are laid out in a contiguous way, just like arrays. The problem here is that the cache is bloated with useless data from the target class.

On the other hand, accessing data from two arrays is very predictable, and the two arrays will be safely loaded into the cache. 
We could bloat the space in between the two arrays with other data, but this won't affect the end result.

## Licensing
This project is licensed under the MIT license. Feel free to fork the project and include any pertinent content.
