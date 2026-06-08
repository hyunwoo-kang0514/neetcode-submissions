class Solution {
    public boolean isAnagram(String s, String t) {

         if (s.length() != t.length()) {
            return false;
        }

        // 두 개의 HashMap을 사용해 문자 빈도를 저장
        Map<Character, Integer> countS = new HashMap<>();
        Map<Character, Integer> countT = new HashMap<>();

        // 각 문자열의 문자 빈도를 계산
        for (int i = 0; i < s.length(); i++) {
            countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i), 0) + 1);
            countT.put(t.charAt(i), countT.getOrDefault(t.charAt(i), 0) + 1);
        }

        // 두 HashMap을 비교하여 서로 다른 값이 있는지 확인
        for (char c : countS.keySet()) {
            if (!countS.get(c).equals(countT.getOrDefault(c, 0))) {
                return false;
            }
        }

        return true;
    }
}
