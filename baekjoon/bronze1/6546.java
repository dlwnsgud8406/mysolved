import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(sc.hasNext()){
            String str = sc.nextLine();
            int x=310,y=420;
            System.out.println(300+" "+420+" "+"moveto");
            System.out.println(310+" "+420+" "+"lineto");
            int fx = 1;
            for(int i=0;i<str.length();i++){
                if(str.charAt(i)=='A'){
                    if(fx==1){
                        y-=10;
                        fx=2;
                    }else if(fx==2){
                        x-=10;
                        fx=3;
                    }else if(fx==3){
                        y+=10;
                        fx=4;
                    }else if(fx==4){
                        x+=10;
                        fx=1;
                    }
                    System.out.println(x+" "+y+" lineto");

                }else{
                    if(fx==1){
                        y+=10;
                        fx=4;
                    }else if(fx==2){
                        x+=10;
                        fx=1;
                    }else if(fx==3){
                        y-=10;
                        fx=2;
                    }else if(fx==4){
                        x-=10;
                        fx=3;
                    }
                    System.out.println(x+" "+y+" lineto");

                }
            }
            System.out.println("stroke");
            System.out.println("showpage");



        }
    }
}
-----------------------------------
©著作权归作者所有：来自51CTO博客作者谙忆的原创作品，请联系作者获取转载授权，否则将追究法律责任
HDOJ 1033 Edge
https://blog.51cto.com/u_14290964/5292647
