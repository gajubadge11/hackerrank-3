import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int lineNum = 1;
    while (in.hasNext()) {
      String input = in.nextLine();
      System.out.println(lineNum + " " + input);
      lineNum++;
    }
  }
}
