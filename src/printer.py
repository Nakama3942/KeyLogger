from src.calendar import calendar


class Printer:
	current_scheme: dict = {}

	def __init__(self, current_scheme: dict):
		self.current_scheme = current_scheme

	def reinit(self, current_scheme: dict):
		self.current_scheme = current_scheme

	def init_string(self):
		return f"<span style='color: #{self.current_scheme['processing_data']};'>" \
		            f"{calendar()} : The program is running for the first time... Configuration initialization:" \
		       f"</span>"

	def config_string(self):
		return f"<span style='color: #{self.current_scheme['processing_data']};'>" \
		            f"{calendar()} : Configuration file created." \
		       f"</span>"

	def log_created_string(self):
		return f"<span style='color: #{self.current_scheme['processing_data']};'>" \
		            f"{calendar()} : Program log created." \
		       f"</span>"

	def run_string(self):
		return f"<span style='color: #{self.current_scheme['processing_data']};'>" \
		            f"{calendar()} : The program is running..." \
		       f"</span>"

	def change_scheme_string(self):
		return f"<span style='color: #{self.current_scheme['color_scheme_change']};'>" \
		            f"{calendar()} : Color scheme changed to {self.current_scheme['SCHEME_NAME']}" \
		       f"</span>"

	def show_program_string(self):
		return f"<span style='color: #{self.current_scheme['hide_show']};'>" \
		            f"{calendar()} : Program displayed." \
		       f"</span>"

	def hide_program_string(self):
		return f"<span style='color: #{self.current_scheme['hide_show']};'>" \
		            f"{calendar()} : The program is hidden." \
		       f"</span>"

	def export_action_string(self):
		return f"<span style='color: #{self.current_scheme['export']};'>" \
		            f"{calendar()} : Export logging action." \
		       f"</span>"

	def export_moving_string(self):
		return f"<span style='color: #{self.current_scheme['export']};'>" \
		            f"{calendar()} : Export logging moving." \
		       f"</span>"

	def start_track_string(self):
		return f"<span style='color: #{self.current_scheme['processing_data']};'>" \
		            f"{calendar()} : Start tracking..." \
		       f"</span>"

	def stop_track_string(self):
		return f"<span style='color: #{self.current_scheme['processing_data']};'>" \
		            f"{calendar()} : Stop tracking..." \
		       f"</span>"

	def reboot_tracking_string(self):
		return f"<span style='color: #{self.current_scheme['reboot']};'>" \
		            f"{calendar()} : Reboot tracking..." \
		       f"</span>"

	def key_pressed_string(self, key: str):
		return f"<span style='color: #{self.current_scheme['key_pressed']};'>" \
		            f"{calendar()} : Key pressed: {key}" \
		       f"</span>"

	def mouse_click_coord_string(self, x: int, y: int, button: str):
		return f"<span style='color: #{self.current_scheme['mouse_clicked']};'>" \
		            f"{calendar()} : Mouse clicked at " \
		            f"<span style='color: #{self.current_scheme['mouse_clicked_coord']};'>" \
		                f"({x}, {y})" \
		            f"</span>" \
		            f" with {button}" \
		       f"</span>"

	def mouse_click_string(self, button: str):
		return f"<span style='color: #{self.current_scheme['mouse_clicked']};'>" \
		            f"{calendar()} : Mouse clicked with {button}" \
		       f"</span>"

	def mouse_release_coord_string(self, x: int, y: int, button: str):
		return f"<span style='color: #{self.current_scheme['mouse_released']};'>" \
		            f"{calendar()} : Mouse released at " \
		            f"<span style='color: #{self.current_scheme['mouse_released_coord']};'>" \
		                f"({x}, {y})" \
		            f"</span>" \
		            f" with {button}" \
		       f"</span>"

	def mouse_release_string(self, button: str):
		return f"<span style='color: #{self.current_scheme['mouse_released']};'>" \
		            f"{calendar()} : Mouse released with {button}" \
		       f"</span>"

	def mouse_scroll_string(self, x: int, y: int, dx: int, dy: int):
		return f"<span style='color: #{self.current_scheme['mouse_scrolled']};'>" \
		            f"{calendar()} : Mouse scrolled at " \
		            f"<span style='color: #{self.current_scheme['mouse_scrolled_coord']};'>" \
		                f"({x}, {y})({dx}, {dy})" \
		            f"</span>" \
		       f"</span>"

	def start_track_moving_string(self):
		return f"<span style='color: #{self.current_scheme['moving_tracking']};'>" \
		            f"{calendar(False)} : Start tracking mouse moving..." \
		       f"</span>"

	def stop_track_moving_string(self):
		return f"<span style='color: #{self.current_scheme['moving_tracking']};'>" \
		            f"{calendar(False)} : Stop tracking mouse moving..." \
		       f"</span>"

	def mouse_move_string(self, x: int, y: int):
		return f"<span style='color: #{self.current_scheme['mouse_moved']};'>" \
		            f"{calendar(False)} : Mouse moved to " \
		            f"<span style='color: #{self.current_scheme['mouse_moved_coord']};'>" \
		                f"({x}, {y})" \
		            f"</span>" \
		       f"</span>"
