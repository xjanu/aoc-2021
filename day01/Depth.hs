import System.Environment
import System.IO

usage :: String -> String
usage progname = "Usage: " ++ progname ++ " <filename>\n"

count :: [Integer] -> Integer
count ls =
    fst $ foldl fun (0, head ls) ls
    where fun (count, prev) next = (count + if next > prev then 1 else 0, next)

depth :: FilePath -> IO ()
depth file = do
    raw <- readFile file
    let nums = read `map` lines raw :: [Integer]
    print $ count nums

main :: IO ()
main = do
    args <- getArgs
    if length args /= 1
    then getProgName >>= hPutStr stderr . usage
    else do
        let file = head args
        depth file
