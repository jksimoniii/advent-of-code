package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func readInputFile(filename string) ([]int, error) {
	file, err := os.Open(filename)

	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var lines []int
	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		lines = append(lines, i)
	}

	return lines, scanner.Err()
}

type Device struct{
	frequency int
}

func (d *Device) ChangeFrequency(delta int) {
	d.frequency += delta
}

func part1(inputValues []int) int {
	d := Device {frequency: 0}
	for _, val := range inputValues {
		d.ChangeFrequency(val)
	}

	return d.frequency
}

func part2(inputValues []int) int {
	d := Device {frequency: 0}
	seenValues := make(map[int]struct{})
	killsig := false
	for {
		for _, val := range inputValues {
			_, exists := seenValues[d.frequency]
			if exists {
				killsig = true
				break
			}
			seenValues[d.frequency] = struct{}{}
			d.ChangeFrequency(val)
		}
		if killsig { break }
	}

	return d.frequency
}

func main() {
	inputValues, err := readInputFile("input.dat")

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Your Result (Part One): ", part1(inputValues))
	fmt.Println("Your Result (Part Two): ", part2(inputValues))
}