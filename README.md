# leetcode_tools
Some tools for leetcode user.

Leetcode中，许多题目给出的输入测试例不能直接被复制进代码中使用，若自己使用IDE进行代码验证，则需要额外的步骤，对输入测试例进行初始化。本项目对部分情况下的初始化步骤进行标准化。
- Develop in python 2.X
- Apply to C++
***
### list2vector.py
- class list2vector()

    以list形式给出输入，将其转换为C++中的vector
    - int2int(): int型list->int型vector
    
        input:
        ```python
        [1, 2, 3, 4]
        ```   
        output:
        ```C++
        int n[4] = {1, 2, 3, 4};
        vector<int> v(n, n+4);
        ```
