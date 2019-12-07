package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
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

func stringToInteger(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		log.Fatal(err)
	}

	return i
}

type Fabric struct {
	area [1000][1000]int
}

type Claim struct {
	id int
	marginLeft int
	marginTop int
	width int
	height int
}

func NewClaim(s string) Claim {
	const REGEX = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
	re := regexp.MustCompile(REGEX)
	match := re.FindStringSubmatch(s)
	return Claim{
		id:  stringToInteger(match[1]),
		marginLeft: stringToInteger(match[2]),
		marginTop: stringToInteger(match[3]),
		width: stringToInteger(match[4]),
		height: stringToInteger(match[5]),
	}
}

func part1(f Fabric) int {
	result := 0
	for x, _ := range f.area[:] {
		for y, _ := range f.area[x][:] {
			if f.area[x][y] > 1 { result++ }
		}
	}

	return result
}

func part2(f Fabric, claims []Claim) int {
	for _, claim := range claims {
		sigkill := false
		for x := 0; x < claim.width; x++ {
			for y := 0; y < claim.height; y++ {
				if f.area[claim.marginLeft + x][claim.marginTop + y] > 1 {
					sigkill = true
					break
				}
			}
			if sigkill { break }
		}
		if !sigkill { return claim.id }
	}
	return 0
}

func initClaims(inputValues []string) []Claim {
	var claims []Claim
	for _, v := range inputValues {
		claims = append(claims, NewClaim(v))
	}

	return claims
}

func initFabric(claims []Claim) Fabric {
	f := Fabric{}
	for _, claim := range claims {
		for x := 0; x < claim.width; x++ {
			for y := 0; y < claim.height; y++ {
				f.area[claim.marginLeft + x][claim.marginTop + y] += 1
			}
		}
	}

	return f
}

func main() {
	inputValues, err := readInputFile("input.dat")

	if err != nil {
		log.Fatal(err)
	}

	claims := initClaims(inputValues)
	fabric := initFabric(claims)
	fmt.Println("Your Result (Part One): ", part1(fabric))
	fmt.Println("Your Result (Part Two): ", part2(fabric, claims))
}