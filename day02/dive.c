#include <errno.h>  // perror
#include <stdio.h>  // fopen, fclose, perror, getline
#include <limits.h> // INT_MAX
#include <stdlib.h> // strtol
#include <string.h> // strncmp

struct coords {
	int fore;
	int depth;
};

struct coords parseline(char *line)
{
	struct coords ret = {0, 0};
	char *rest;
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

	long i = strtol(rest, NULL, 10);
	if (i > INT_MAX || i < 0) {
		fprintf(stderr, "Parse error: int out of range: '%ld'\n", i);
		return ret;
	}
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

int dive(FILE *fp)
{
	int fore = 0, depth = 0;
	char *line = NULL;
	size_t n = 0;

	while (getline(&line, &n, fp) != -1) {
		struct coords delta = parseline(line);
		fore += delta.fore;
		depth += delta.depth;
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
	FILE *fp = fopen("input", "r");
	if (fp == NULL) {
		perror("fopen");
		return 1;
	}

	printf("%d\n", dive(fp));

	fclose(fp);

	return 0;
}
