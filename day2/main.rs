use std::fmt::Write;

fn main() {
    let lines = std::io::stdin().lines().next().unwrap().unwrap();

    let mut count1 = 0;
    let mut count2 = 0;

    for part in lines.split(",").filter(|s| !s.is_empty()) {
        let (l, r) = part.split_once("-").unwrap();
        let l = l.parse::<usize>().unwrap();
        let r = r.parse::<usize>().unwrap();
        let mut s = String::new();
        for i in l..=r {
            s.clear();
            write!(s, "{i}").unwrap();

            let mut invalid1 = false;
            let mut invalid2 = false;

            for n in 1..s.len() {
                if s.len().is_multiple_of(n) {
                    let mut chunks = s.as_bytes().chunks(n);
                    let first = chunks.next().unwrap();
                    let rep = chunks.all(|w| w == first);
                    invalid1 |= rep && s.len() == n * 2;
                    invalid2 |= rep;
                }
            }
            if invalid1 {
                count1 += i;
            }
            if invalid2 {
                count2 += i;
            }
        }
    }

    println!("{count1} {count2}");
}
