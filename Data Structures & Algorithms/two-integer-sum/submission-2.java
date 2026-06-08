class Solution {
    public int[] twoSum(int[] arr, int target) {

         HashMap<Integer, Integer> hash = new HashMap<>();
        int diff = 0;

        for(int i = 0; i < arr.length; i++) {
            diff = target - arr[i];
            if(hash.containsKey(diff)) {
                return new int[] {hash.get(diff), i};
            }
            hash.put(arr[i], i);
        }
        
        return new int[] {};

    }
}
