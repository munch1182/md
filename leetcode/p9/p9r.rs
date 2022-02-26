fn main(){
    println!("{}",is_palindrome(121));
    println!("{}",is_palindrome(-121));
    println!("{}",is_palindrome(1221));

    println!("{}",is_palindrome2(121));
    println!("{}",is_palindrome2(-121));
    println!("{}",is_palindrome2(1221));

    println!("{}",is_palindrome3(121));
    println!("{}",is_palindrome3(-121));
    println!("{}",is_palindrome3(1221));
}

fn is_palindrome(x: i32) -> bool {
    let str = x.to_string();
    str == str.chars().rev().collect::<String>()
}

fn is_palindrome2(x: i32) -> bool {
    if x < 0 {
        return false;
    }
    let mut list = Vec::new();
    let mut y = x;
    while y > 0 {
        list.push(y % 10);
        y = y / 10;
    }
    let l = list.len();
    for i in 0..(l/2) {
        if list.get(i).unwrap() != list.get(l -i -1).unwrap() {
            return false;
        }
    }
    true
}

fn is_palindrome3(x: i32) -> bool {
    if x < 0 || (x !=0 && x % 10 == 0){
        return false;
    }
    let mut y = x;
    let mut z = 0;
    while z < y {
        z = z*10+y%10;
        y /= 10;
    }
    return z == y || z/10 == y;
}