import java.util.Arrays;
import java.util.HashSet;
    
class Solution { 
    public int[] solution(int[] numbers) {
        HashSet<Integer> arr = new HashSet<>();
		
		for (int i = 0; i < numbers.length-1; i++) {
			for (int j = i + 1; j < numbers.length; j++) {
				arr.add(numbers[i] + numbers[j]);
			}
		}
		
		int[] answer = new int[arr.size()];
		int idx = 0;
		
		for(int num : arr) {
			answer[idx++] = num;
		}
		
		Arrays.sort(answer);
        return answer;
    }
}