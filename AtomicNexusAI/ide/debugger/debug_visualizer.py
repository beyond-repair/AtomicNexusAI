# debug_visualizer.py
import plotly.express as px

class DebugVisualizer:
    def visualize(self, agent_state: object) -> None:
        fig = px.sunburst(
            agent_state.decision_tree,
            path=['task', 'model_used'],
            values='exec_time'
        )
        fig.show()