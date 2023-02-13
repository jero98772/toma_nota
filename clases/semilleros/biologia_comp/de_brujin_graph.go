package main
import "fmt"
type void struct{}
type pair struct{
	firts string
	second string
}
func buildKMer(txt string,k int) []string{
    mers:=make([]string,0)
    for i:=0;i<len(txt)-k+1;i++{   	
	mers=append(mers,txt[i:k+i])
    }
    return mers
}
/*
def debruijnize(reads):
    nodes = set()
    not_starts = set()
    edges = []
    for r in reads:
        r1 = r[:-1]
        r2 = r[1:]
        nodes.add(r1)
        nodes.add(r2)
        edges.append((r1,r2))
        not_starts.add(r2)
    return (nodes,edges,list(nodes-not_starts))

func debruijnize(txt string){
	nodes:=make(map[string]void)
	not_starts:=make(map[string]void)
	edges:=make(pair
}*/
func debruijnize(reads []string) (nodes, edges []string, notStarts []string) {
	nodeSet := make(map[string]bool)
	notStartSet := make(map[string]bool)
	for _, r := range reads {
		r1 := r[:len(r)-1]
		r2 := r[1:]
		nodeSet[r1] = true
		nodeSet[r2] = true
		edges = append(edges, r1+" "+r2)
		notStartSet[r2] = true
	}
	for node := range nodeSet {
		nodes = append(nodes, node)
	}
	for node := range nodeSet {
		if !notStartSet[node] {
			notStarts = append(notStarts, node)
		}
	}
	return
}
func makeNodeEdgeMap(edges []string) map[string][]string {
	nodeEdgeMap := make(map[string][]string)
	for _, edge := range edges {
		n := edge[:string.Index(edge, " ")]
		if nodeEdgeMap[n] != nil {
			nodeEdgeMap[n] = append(nodeEdgeMap[n], edge[strings.Index(edge, " ")+1:])
		} else {
			nodeEdgeMap[n] = []string{edge[strings.Index(edge, " ")+1:]}
		}
	}
	return nodeEdgeMap
}


func eulerianTrail(nemap map[string][]string, v string) []string {
	resultTrail := []string{}
	start := v
	resultTrail = append(resultTrail, start)

	for {
		trail := []string{}
		previous := start

		for {
			if _, ok := nemap[previous]; !ok {
				break
			}

			next := nemap[previous][len(nemap[previous])-1]
			nemap[previous] = nemap[previous][:len(nemap[previous])-1]
			if len(nemap[previous]) == 0 {
				delete(nemap, previous)
			}
			trail = append(trail, next)
			if next == start {
				break
			}
			previous = next
		}

		fmt.Println(trail)
		index := -1
		for i, node := range resultTrail {
			if node == start {
				index = i
				break
			}
		}
		resultTrail = append(resultTrail[:index+1], trail...)
		resultTrail = append(resultTrail[:index+1+len(trail)], resultTrail[index+1:]...)

		if len(nemap) == 0 {
			break
		}

		foundNewStart := false
		for _, n := range resultTrail {
			if _, ok := nemap[n]; ok {
				start = n
				foundNewStart = true
				break
			}
		}

		if !foundNewStart {
			fmt.Println("error")
			fmt.Println("resultTrail", resultTrail)
			fmt.Println(nemap)
			break
		}
	}
	return resultTrail
}
func assembleTrail(trail []string) string {
	if len(trail) == 0 {
		return ""
	}
	result := trail[0][:len(trail[0])-1]
	for _, node := range trail {
		result += node[len(node)-1:]
	}
	return result
}

func testAssemblyDebruijn(t string, k int) string {
	reads := buildKMer(t, k)
	_,G,_ := debruijnize(reads)
	//v := visualizeDebruijn(G)
	nemap := makeNodeEdgeMap(G[1])
	fmt.Println(G)
	//fmt.Println(v)
	var start string
	if len(G[2]) > 0 {
		start = G[2][0]
	} else {
		start = G[0][0]
	}
	trail := eulerianTrail(nemap, start)
	return assembleTrail(trail)
}
func main(){
	a:=buildKMer("ATCGTTGCGCGACCG",4)
	nodes,edges,dijuntsetnodes:=debruijnize(a)	
	fmt.Println(len(nodes),len(edges),len(dijuntsetnodes))
	makeNodeEdgeMap(edges)
}


