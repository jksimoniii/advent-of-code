package main

import (
"bufio"
"fmt"
"log"
"os"
"regexp"
"sort"
"strconv"
//"time"
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

type LogEntry struct {
	date string
	guardId int
	asleepAt []int
	awakeAt []int
	timeAsleep int
}

type Log struct {
	entries []*LogEntry
}

func (log *Log)GetOrCreateLogEntry(date string) (*LogEntry, bool) {
	for _, e := range log.entries {
		if e.date == date { return e, false }
	}
	entry := LogEntry{date: date}
	return &entry, true
}

func (log *Log)CreateOrUpdateLogEntry(s string) {
	dateRegexp := regexp.MustCompile(`\[\d+\-(\d+\-\d+) \d+:(\d+)]`)
	onShiftRegexp := regexp.MustCompile(`Guard #(\d+)`)
	sleepRegexp := regexp.MustCompile(`falls asleep`)
	wakeRegexp := regexp.MustCompile(`wakes up`)

	parts := dateRegexp.FindStringSubmatch(s)
	date := parts[1]
	minute, _ := strconv.Atoi(parts[2])
	entry, created := log.GetOrCreateLogEntry(date)

	if onShiftRegexp.MatchString(s) {
		parts := onShiftRegexp.FindStringSubmatch(s)
		guardId, _ := strconv.Atoi(parts[1])
		entry.guardId = guardId
	} else if sleepRegexp.MatchString(s) {
		parts = sleepRegexp.FindStringSubmatch(s)
		entry.asleepAt = append(entry.asleepAt, minute)
	} else if wakeRegexp.MatchString(s) {
		parts = wakeRegexp.FindStringSubmatch(s)
		entry.awakeAt = append(entry.awakeAt, minute)
	}

	if created {
		log.entries = append(log.entries, entry)
	}
}

func part1(inputValues []string) int {
	log := Log{}
	for _, input := range inputValues {
		log.CreateOrUpdateLogEntry(input)
	}

	sleepiestEntry := log.entries[0]
	for _, e := range log.entries {
		sort.Ints(e.awakeAt)
		sort.Ints(e.asleepAt)

		timeAsleep := 0
		for i, v := range e.asleepAt {
			timeAsleep += e.awakeAt[i] - v
		}
		e.timeAsleep = timeAsleep

		if sleepiestEntry.timeAsleep < e.timeAsleep {
			sleepiestEntry = e
		}
	}
	fmt.Println(sleepiestEntry)
	return 1
}

func main() {
	inputValues, err := readInputFile("input.dat")

	if err != nil {
		log.Fatal(err)
	}



	fmt.Println("Your Result (Part One): ", part1(inputValues))
	//fmt.Println("Your Result (Part Two): ", part2(fabric, claims))
}