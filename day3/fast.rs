use std::io::{BufRead, Result};

fn main() -> Result<()> {
    let mut stdin = std::io::stdin().lock();

    let mut table = [0; 13];

    let mut part1 = 0;
    let mut part2 = 0;
    while let b = stdin.fill_buf()?
        && !b.is_empty()
    {
        for &b in b {
            if b == b'\n' {
                part1 += table[0];
                part2 += table[10];
                table = [0; _];
            } else {
                let d = (b - b'0') as u64;
                let prev = table;
                for i in 0..12 {
                    table[i] = table[i].max(prev[i + 1] * 10 + d);
                }
            }
        }

        let l = b.len();
        stdin.consume(l);
    }
    part1 += table[0];
    part2 += table[10];

    println!("{part1} {part2}");

    Ok(())
}
