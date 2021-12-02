#include <errno.h>  // perror
#include <stdio.h>  // fopen, fclose, perror, getline
#include <limits.h> // INT_MAX
#include <stdlib.h> // strtol
#include <string.h> // strncmp

char usage[] =
	"Usage: %s [<part>] <filename>\n"
	"Where <part> is either 1 or 2, depending on the part of the challenge,\n"
    "             default value is 1.\n"
    "      <filename> is the path to the puzzle input file.\n";

struct coords {
	int fore;
	int depth; // For part 2, this is actually change in aim
};

struct coords parseline(char *line)
{
	struct coords ret = {0, 0};
	char *rest;

	// Check if line begins with a valid direction, separate the rest of the line
	if (strncmp(line, "forward ", 8) == 0) {
		rest = line + 8;
	} else if (strncmp(line, "down ", 5) == 0) {
		rest = line + 5;
	} else if (strncmp(line, "up ", 3) == 0) {
		rest = line + 3;
	} else {
		fprintf(stderr, "Failed to parse line: '%s'\n", line);
		return ret;
	}

	// Parse distance
	long i = strtol(rest, NULL, 10);
	if (i > INT_MAX || i < 0) {
		fprintf(stderr, "Parse error: int out of range: '%ld'\n", i);
		return ret;
	}

	// Fill coords based on direction and distance
	switch (line[0]) {
	case 'f':
		ret.fore = i;
		break;
	case 'd':
		ret.depth = i;
		break;
	case 'u':
		ret.depth = -i;
		break;
	default: // unreachable
		break;
	}

	return ret;
}

int dive(FILE *fp, int part)
{
	int fore = 0, depth = 0, aim = 0;
	char *line = NULL;
	size_t n = 0;

	// Parse each line and modify coords
	while (getline(&line, &n, fp) != -1) {
		struct coords delta = parseline(line);
		if (part == 1) {
	            fore += delta.fore;
                depth += delta.depth;
		} else {
			aim += delta.depth;
			fore += delta.fore;
			depth += aim * delta.fore;
		}
		if (depth < 0) {
			depth = 0;
		}
	}
	if (errno != 0) {
		perror("getline");
	}
	free(line);

	return fore * depth;
}

int main(int argc, char* argv[])
{
	char *filename;
	int part;

	// Parse cmdline arguments
	if (argc <= 1 || argc > 3) {
		fprintf(stderr, usage, argv[0]);
		return 2;
	} else if (argc == 2) {
		part = 1;
		filename = argv[1];
	} else {
		if (strcmp(argv[1], "1") == 0) {
			part = 1;
		} else if (strcmp(argv[1], "2") == 0) {
			part = 2;
		} else {
			fprintf(stderr, usage, argv[0]);
			return 2;
		}
		filename = argv[2];
	}

	FILE *fp = fopen(filename, "r");
	if (fp == NULL) {
		perror("fopen");
		return 1;
	}

	printf("%d\n", dive(fp, part));

	fclose(fp);

	return 0;
}
