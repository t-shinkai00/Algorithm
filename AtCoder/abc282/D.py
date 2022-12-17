from copy import deepcopy
#グラフオブジェクトを表すクラス
class Graph:
  def __init__(self, edges = None, n = 0):
    self.n = n  #グラフ内のノードの総数
    self.adjList = [[] for _ in range(n)]  #隣接リストを表すリストのリスト

    for (src, dest) in edges:
      self.adjList[src].append(dest)
      self.adjList[dest].append(src)


#頂点`v`から始まるグラフでDFSを実行します
def DFS(graph, v, discovered, color, adjList):

  #はすべてのエッジに対して実行します(v、u)
  for u in adjList[v]:

    # 頂点`u`が初めて探索される場合は
    if not discovered[u]:

      #は、現在のノードを検出済みとしてマークします
      discovered[u] = True

      #の現在のノードは、その親とは反対の色になります
      color[u] = not color[v]

      # `v`をルートとするサブツリーのDFSがfalseを返す場合は
      if not DFS(graph, u, discovered, color, adjList):
        return False

    #頂点がすでに検出されている場合、および
    #頂点`u`と`v`が同じである場合、グラフは2部グラフではありません
    elif color[v] == color[u]:
      return False

  return True


# DFSを使用してグラフが2部グラフであるかどうかを確認する#関数
def is_bipartite(graph, u, v):
  adjList = deepcopy(graph.adjList)
  # 辺の追加
  adjList[u].append(v)
  adjList[v].append(u)

  # 頂点が検出されたかどうかを追跡する
  discovered = [False] * graph.n

  #は、DFSの各頂点に割り当てられた色(0または1)を追跡します
  color = [False] * graph.n

  #は、グラフが接続され、無向であるため、任意のノードから開始します
  src = 0

  #は、ソース頂点を検出済みとしてマークし、その色を0(偽)に設定します
  discovered[src] = True
  color[src] = False

  #呼び出しDFSプロシージャ
  return DFS(graph, src, discovered, color, adjList)


if __name__ == '__main__':
  n, m = map(int, input().split())

  edges = []
  for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u-1,v-1))

  graph = Graph(edges, n)
  # print(graph.adjList)

  cnt = 0
  for u in range(n-1):
    for v in range(u+1, n):
      if v not in graph.adjList[u] and is_bipartite(graph, u, v):
        print('bipartite: ', u, v)
        cnt += 1
  print(cnt)
  # print(graph.adjList)
