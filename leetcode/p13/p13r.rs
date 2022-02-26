fn main(){
    assert_eq!(roman_to_int("MCMXCIV".to_string()) , 1994);
    assert_eq!(roman_to_int("LVIII".to_string()) , 58);
    assert_eq!(roman_to_int("IX".to_string()) , 9);
}

fn roman_to_int(s: String) -> u32 {
    let key = vec!['I','V','X','L','C','D','M'];
    let value = vec![1,5,10,50,100,500,1000];
    let map:std::collections::HashMap<&char,&u32> = key.iter().zip(value.iter()).collect();

    let mut result:u32 = 0;
    let mut last:u32 = 0;
    for c in s.chars(){
        let i = *map.get(&c).unwrap();
        result += i;
        if last < *i {
            result -= i + last - (i-last);
        }
        last = *i;
    }
    return result
}

fn roman_to_int3(s: String) -> u32 {
    let key = vec!['I','V','X','L','C','D','M'];
    let value = vec![1,5,10,50,100,500,1000];
    let map:std::collections::HashMap<&char,&u32> = key.iter().zip(value.iter()).collect();

    let mut result:u32 = 0;
    let mut last:u32 = 0;
    for c in s.chars(){
        let i = *map.get(&c).unwrap();
        result += i;
        if last < *i {
            result -= i + last - (i-last);
        }
        last = *i;
    }
    return result
}

fn roman_to_int2(s: String) -> u32 {
    let mut map= std::collections::HashMap::new();
    map.insert('I',1);
    map.insert('V',5);
    map.insert('X',10);
    map.insert('L',50);
    map.insert('C',100);
    map.insert('D',500);
    map.insert('M',1000);
    let mut result:u32 = 0;
    let mut last:u32 = 0;
    for c in s.chars(){
        let i = *map.get(&c).unwrap();
        result += i;
        if last < i {
            result -= i + last - (i-last);
        }
        last = i;
    }
    return result
}
