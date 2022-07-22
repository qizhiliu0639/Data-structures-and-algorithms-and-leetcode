# Arrays.sort()

用法：
```java
int[] arr = new int[]{5, 3, 2, 1, 4};
Arrays.sort(arr);
System.out.println(Arrays.toString(arr));
```

output:
```java
[1, 2, 3, 4, 5]
```

## 入口：

查看Arrays.sort()函数，代码如下：

```java
public static void sort(int[] a) {
        DualPivotQuicksort.sort(a, 0, a.length - 1, null, 0, 0);
    }
```

`DualPivotQuicksort`译为「双轴快排」，之前我们介绍的快速排序算法属于「单轴快排」。顾名思义，双轴快排每轮选取两个轴，将数组分为三个区域，这样就能每轮排好两个基数，通常效率比单轴快排更高。

但`DualPivotQuicksort`类中并不是只使用了双轴快排算法，它会根据输入数据的规模、结构化程度来采用不同的排序算法。