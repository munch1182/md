fn main(){
    println!("{:?}",two_sum(vec![1,12,101,111], 102));
    println!("{:?}",two_sum2(vec![1,12,101,111], 102));
}

fn two_sum(nums:Vec<i32>,target:i32)->Vec<i32>{
    for (i,num) in nums.iter().enumerate() {
        for (j,n) in nums[i+1..].iter().enumerate() {
            if num + n == target {
               return vec![i as i32,j as i32]
            }
        }
    }
    vec![-1,-1]
}

fn two_sum2(nums:Vec<i32>,target:i32)->Vec<i32>{
    let mut map = std::collections::HashMap::new();
    for (i,num) in nums.iter().enumerate(){
        let result = target - num;
        if map.contains_key(&result) {
            if let Some(j) = map.get(&result) {
                return vec![*j, i as i32];
            }
        } else {
            map.insert(num, i as i32);
        }
    }
    vec![-1,-1]
}