# CMPS 2200 Recitation 05
## Answers

**Name:** Chuong Hoang Pham
_________________________

Place all written answers from `recitation-05.md` here for easier grading.




- **3) (2 pts)** What is the work and span of `get_positions`? (assume our more efficient version of `scan` from class)

    Since `scan` has the work $O(n)$ and span $O(\log n)$ for n is the length of the sequence, in this problem, the length is $k$ which is the max number in the list. Therefore,

    - Work: $O(k)$

    - Span: $O(\log k)$

- **5) (2 pts)** What is the work and span of `construct_output`?

    For `construct_output`, we use for loop to iterate the original list, get the number and check it's index from `positions` array, then update the result array and `positions` array. Since it's sequential operation, the work and span are the same, which is $O(n)$. Therefore, 

    - Work: $O(n)$

    - Span: $O(n)$

- **6) (2 pts)** What is the work and span of `supersort`?

    For `supersort`, we combine the steps, which `count_values` is $O(n+k)$, `get_positions` is $O(k)$ for work and $O(\log k)$ for span, and `construct_output` is $O(n)$. Therefore,

    - Work: $O(n + k) + O(k) + O(n) = O(n + k)$

    - Span: $O(n) + O(\log k) + O(n) = O(n + \log k)$

- **8) (2 pts)** What is work and span of `count_values_mr`?

    For `count_values_mr`, we use map-reduce:
    - **Map phase (`count_map`)**: maps all $n$ elements, taking $O(n)$ work and $O(1)$ span.
    - **Collect phase**: groups matching keys by sorting, taking $O(n \log n)$ work and $O(\log^2 n)$ span.
    - **Reduce phase (`count_reduce`)**: sums each group using parallel tree reduce, taking $O(n)$ work and $O(\log n)$ span across all items.
    - **Final list**: builds the output array of length $k+1$ by looking up each count in $O(k)$ work and $O(1)$ span.

    - Work: $O(n) + O(n \log n) + O(n) + O(k) = O(n \log n + k)$

    - Span: $O(1) + O(\log^2 n) + O(\log n) + O(1) = O(\log^2 n)$
