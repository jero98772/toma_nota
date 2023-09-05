package geometry;

public class Edge {
    public int start;
    public int end;

    public Edge(int start, int end) {
        this.start = start;
        this.end = end;
    }

    public String toString() {
        return "(" + start + ", " + end + ")";
    }
}
