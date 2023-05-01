main :: IO ()
main = do
  contents <- readFile "day01.txt"
  let input = map read . words $ contents
  print $ countIncreases input
  print $ countIncreases2 input

countIncreases :: [Int] -> Int
countIncreases = countIncreases' 0
  where
    countIncreases' :: Int -> [Int] -> Int
    countIncreases' n [] = n
    countIncreases' n [_] = n
    countIncreases' n (r:rs)
      | head rs > r = countIncreases' (n + 1) rs
      | otherwise = countIncreases' n rs

countIncreases2 :: [Int] -> Int
countIncreases2 = countIncreases2' 0
  where
    countIncreases2' :: Int -> [Int] -> Int
    countIncreases2' n [] = n
    countIncreases2' n [_] = n
    countIncreases2' n [_, _] = n
    countIncreases2' n [_, _, _] = n
    countIncreases2' n (r1:r2:r3:rs)
      | head rs > r1 = countIncreases2' (n + 1) (r2:r3:rs)
      | otherwise = countIncreases2' n (r2:r3:rs)