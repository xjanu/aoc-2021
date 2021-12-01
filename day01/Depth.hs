import System.Environment
import System.IO

usage :: String -> String
usage progname =
    "Usage: " ++ progname ++ " [<part>] <filename>\n" ++
    "Where <part> is either 1 or 2, depending on the part of the challenge,\n" ++
    "             default value is 1.\n" ++
    "      <filename> is the path to the puzzle input file.\n"

-- Count the number of increases
count :: [Integer] -> Integer
count ls =
    fst $ foldl fun (0, head ls) ls
    where fun (count, prev) next = (count + if next > prev then 1 else 0, next)

-- Calculate the sliding window
sliding :: [Integer] -> [Integer]
sliding (x:y:ls) =
    third $ foldl fun (x, y, []) ls
    where fun (x, y, ls) z = (y, z, ls ++ [x + y + z])
          third (_, _, x) = x
sliding _ = []

-- Read file and process input
depth :: Int -> FilePath -> IO ()
depth part file = do
    raw <- readFile file
    let nums = read `map` lines raw :: [Integer]
    if part == 2
    then print $ count $ sliding nums
    else print $ count nums

-- Parse args
parseArgs :: [String] -> (Int, FilePath)
parseArgs [part, file] = (read part, file)
parseArgs [file]       = (1, file)

main :: IO ()
main = do
    args <- getArgs
    if null args || length args > 2
    then getProgName >>= hPutStr stderr . usage
    else do
        let (part, file) = parseArgs args
        if part /= 1 && part /= 2
        then getProgName >>= hPutStr stderr . usage
        else depth part file
