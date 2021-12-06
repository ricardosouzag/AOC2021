import System.IO  
import Control.Monad

main = do  
        contents <- readFile "day1.txt"
        let input = map read . words $ contents
        print . countIncreases input $ 0
        print . countIncreases2 input $ 0

countIncreases :: [Int] -> Int -> Int                      
countIncreases [r] n    = n
countIncreases (r:rs) n | head rs > r = countIncreases rs (n+1)
                        | otherwise = countIncreases rs n


countIncreases2 :: [Int] -> Int -> Int                      
countIncreases2 [r1,r2,r3] n = n
countIncreases2 (r1:r2:r3:rs) n | head rs > r1 = countIncreases2 (r2:r3:rs) (n+1)
                                | otherwise = countIncreases2 (r2:r3:rs) n