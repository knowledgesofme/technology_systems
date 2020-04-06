```plantuml
digraph name {
    "node1" -> "node2"
    subgraph name1 {
        "node3" -> "node2"
        "node4" -> "node2"
    }
}
```