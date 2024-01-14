class Solution {
    public int solution(String s) {
        int min = s.length();

        for (int i = 1; i <= s.length() / 2; i++) {
            int length = 0;

            for(int j = 0; j + i <= s.length();){
                int h = j + i;
                int count = 1;
                String seg = s.substring(j, j + i);
                
                while(
                    h + i <= s.length()
                    && seg.equals(s.substring(h, h + i))
                ){
                    h += i;
                    count++;
                } 
                if(count == 1) {
                    length += i;
                } else {
                    length += i + String.valueOf(count).length();  
                }
                j = h;
            }
            if(s.length() % i != 0) {
                length += s.length() % i; 
            }
            min = Math.min(min, length);
        }

        return min;
    }
}