# 函数的参数检查
1. 参数个数不对时，Python解释器将会自动检查出来，并抛出TypeError
2. 参数类型不对时，除了内置函数，其他自定义函数Python解释器将无法检查出来。

# 实现类型检查
当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善  

因此需要使用内置函数 isintance() 对类型进行检查

# 函数总结
1. 定义函数时，需要确定函数名和参数个数；

2. 如果有必要，可以先对参数的数据类型做检查；

3. 函数体内部可以用return随时返回函数结果；

4. 函数执行完毕也没有return语句时，自动return None。

5. 函数可以同时返回多个值，但其实就是一个tuple。