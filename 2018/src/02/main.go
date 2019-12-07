package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func readInputFile(filename string) ([]string, error) {
	file, err := os.Open(filename)

	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		i := scanner.Text()
		lines = append(lines, i)
	}

	return lines, scanner.Err()
}

func levenshtein(str1, str2 string) int {
	s1len := len(str1)
	s2len := len(str2)
	column := make([]int, len(str1)+1)

	for y := 1; y <= s1len; y++ {
		column[y] = y
	}
	for x := 1; x <= s2len; x++ {
		column[0] = x
		lastkey := x - 1
		for y := 1; y <= s1len; y++ {
			oldkey := column[y]
			var incr int
			if str1[y-1] != str2[x-1] {
				incr = 1
			}

			column[y] = minimum(column[y]+1, column[y-1]+1, lastkey+incr)
			lastkey = oldkey
		}
	}
	return column[s1len]
}

func minimum(a, b, c int) int {
	if a < b {
		if a < c {
			return a
		}
	} else {
		if b < c {
			return b
		}
	}
	return c
}


func Filter(vs []string, f func(string) bool) []string {
	vsf := make([]string, 0)
	for _, v := range vs {
		if f(v) {
			vsf = append(vsf, v)
		}
	}
	return vsf
}

func part1(inputValues []string) (int, []string) {
	mul1, mul2 := 0, 0
	var matches []string
	for _, val := range inputValues {
		hasTwo, hasThree := false, false
		for _, c := range val {
			hasTwo = hasTwo || strings.Count(val, string(c)) == 2
			hasThree = hasThree || strings.Count(val, string(c)) == 3

			if hasTwo && hasThree {
				break
			}
		}
		if hasTwo { mul1 += 1}
		if hasThree { mul2 += 1}

		if hasTwo || hasThree {matches = append(matches, val)}
	}

	return mul1 * mul2, matches
}

func part2(ids []string) string {
	var commonLetters []string
	for i, id := range ids {
		matches := Filter(ids[i+1:], func (v string) bool {
			return levenshtein(id, v) == 1
		})
		if len(matches) == 1 {
			for i, c := range matches[0] {
				if rune(id[i]) == c { commonLetters = append(commonLetters, string(c))}
			}
		}
	}

	return strings.Join(commonLetters, "")
}

func main() {
	inputValues, err := readInputFile("input.dat")

	if err != nil {
		log.Fatal(err)
	}

	checksum, matches := part1(inputValues)
	fmt.Println("Your Result (Part One): ", checksum)
	fmt.Println("Your Result (Part Two): ", part2(matches))
}