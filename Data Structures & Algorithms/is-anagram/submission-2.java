class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()) {
            return false;
        }

        char[] c1 = new char[s.length()];
        char[] c2 = new char[t.length()];

        
        for(int i = 0; i < s.length(); i++) {
            c1[i] = s.charAt(i);
            c2[i] = t.charAt(i);
        }

        for(int i = 0; i < s.length(); i++) {
            for(int j = 0; j < s.length(); j++) {
                if(c1[i] == c2[j]) {
                   c2[j] = ' ';
                   break;
                }
                else if(j == s.length() -1 && c1[i] != c2[j]) {
                   return false;
                }
            }
        }

        return true;

    }
}
