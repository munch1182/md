fun main(){
    println(isPalindrome(121))
    println(isPalindrome(-121))
    println(isPalindrome(1221))

    println(isPalindrome2(121))
    println(isPalindrome2(-121))
    println(isPalindrome2(1221))

    println(isPalindrome3(121))
    println(isPalindrome3(-121))
    println(isPalindrome3(1221))
}

fun isPalindrome(x: Int): Boolean {
    return x.toString() == x.toString().reversed()
}

fun isPalindrome2(x: Int): Boolean {
    if(x<0){
        return false
    }
    val list = arrayListOf<Int>()
    var y = x
    while( y > 0){
        list.add(y % 10)
        y /= 10
    }
    val size = list.size
    for (i in 0 until size / 2) {
        if (list[i] != list[size - i - 1]){
            return false
        }
    }
    return true
}

fun isPalindrome3(x: Int): Boolean {
    if( x < 0 || (x!=0 && x%10==0)){
        return false
    }
    var y = x
    var z = 0
    while (z < y){
        z = z*10 + y%10
        y /= 10
    } 
    return y == z || y == z/10
}