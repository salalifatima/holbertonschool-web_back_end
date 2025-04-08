export default function taskBlock(trueOrFalse) {
  let task1 = false;
  let task2 = true;

  if (trueOrFalse) {
    task1 = true;  
    task2 = false;
  }

  return [task1, task2];
}
