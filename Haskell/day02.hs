import Data.List (unfoldr)

main :: IO ()
main = do
  contents <- readFile "day02.txt"
  let input = words contents
  let instructions = combineInstructions input
  let coords1 = applyInstructions1 instructions (0, 0)
  print $ product (pairToList coords1)
  let coords2 = applyInstructions2 instructions (0, 0, 0)
  print $ product (pairToList (dropThird coords2))

pairToList :: (a, a) -> [a]
pairToList (x, y) = [x, y]

dropThird :: (a, b, c) -> (a, b)
dropThird (x, y, _) = (x, y)

readInt :: String -> Int
readInt = read

combineInstructions :: [String] -> [(Char, Int)]
combineInstructions = unfoldr parseInstruction
  where
    parseInstruction [] = Nothing
    parseInstruction [_] = Just (error "Invalid instruction format", error "Invalid instruction format")
    parseInstruction (str : n : rest) = Just ((head str, readInt n), rest)

applyInstructions1 :: [(Char, Int)] -> (Int, Int) -> (Int, Int)
applyInstructions1 [] (p, d) = (p, d)
applyInstructions1 ((ch, n) : rest) (p, d)
  | ch == 'f' = applyInstructions1 rest (p + n, d)
  | ch == 'd' = applyInstructions1 rest (p, d + n)
  | otherwise = applyInstructions1 rest (p, d - n)

applyInstructions2 :: [(Char, Int)] -> (Int, Int, Int) -> (Int, Int, Int)
applyInstructions2 [] (p, d, a) = (p, d, a)
applyInstructions2 ((ch, n) : rest) (p, d, a)
  | ch == 'f' = applyInstructions2 rest (p + n, d + (n * a), a)
  | ch == 'd' = applyInstructions2 rest (p, d, a + n)
  | otherwise = applyInstructions2 rest (p, d, a - n)
