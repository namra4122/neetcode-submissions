class Solution {

    public String encode(List<String> strs) {
        StringBuilder strBuild = new StringBuilder();

        for(String str: strs){
            strBuild.append(str.length()).append("#").append(str);
        }

        return strBuild.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<String>();
        int i = 0;
        while(i<str.length()){
            int j = i;
            while(str.charAt(j) != '#') j++;

            int len = Integer.valueOf(str.substring(i,j));

            i = j+len+1;

            res.add(str.substring(j+1,i));
        }

        return res;
    }
}
