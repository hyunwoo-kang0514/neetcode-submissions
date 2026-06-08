class Solution {
    public boolean hasDuplicate(int[] nums) {

        HashSet<Integer> hashset = new HashSet<>();
        
        for (int n : nums) {
            if (hashset.contains(n)) {
                return true;  // 중복된 값이 발견되면 true 반환
            }
            hashset.add(n);  // 중복이 없으면 해시셋에 추가
        }
        
        return false;  // 중복이 없으면 false 반환
 
    }
}
