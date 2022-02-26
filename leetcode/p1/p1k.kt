fun main(){
    System.out.println(twoSum(intArrayOf(1,10,111,112),112).joinToString())
    System.out.println(twoSum(intArrayOf(1,10,111,111,112),112).joinToString())
    System.out.println(twoSum(intArrayOf(111,10,1,112),112).joinToString())

    System.out.println(twoSum2(intArrayOf(1,10,111,112),112).joinToString())
    System.out.println(twoSum2(intArrayOf(1,10,111,111,112),112).joinToString())
    System.out.println(twoSum2(intArrayOf(111,10,1,112),112).joinToString())
}


fun twoSum(nums: IntArray, target: Int): IntArray {
    nums.forEachIndexed { index, num ->
        for (j in index + 1 until nums.size) {
            if (num + nums[j] == target){
                return intArrayOf(index,j)
            }
        }
    }
    return intArrayOf(-1,-1)
}

fun twoSum2(nums:IntArray,target:Int):IntArray {
    val map = hashMapOf<Int,Int>()
    nums.forEachIndexed{index,num->
        val result = target - num
        if(map.contains(result)){
            return intArrayOf(map[result]!!,index)
        }
        map[num] = index
    }
    return intArrayOf(-1,-1)
}