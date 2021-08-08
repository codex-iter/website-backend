from model.event import Event
import datetime
# Testing

cats = ['../testingAssets/cat 1.jpeg','../testingAssets/cat 3.jpeg']
ev = Event()
_title = "Event alice"
_des = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum hendrerit consectetur. Aliquam tincidunt nisi in metus sodales cursus. Etiam sed dui feugiat, volutpat mauris sit amet, auctor nulla. Vivamus iaculis metus lobortis tortor viverra, sed venenatis metus sodales. Proin bibendum auctor aliquam. Integer blandit dolor lectus, ut aliquet diam sagittis eu. Donec sodales, justo nec sollicitudin pharetra, sem eros finibus sapien, in sollicitudin urna neque id arcu. Phasellus malesuada lectus felis, at dictum neque feugiat eu. Duis ut aliquam nibh, a porttitor justo. "
_images = cats
_date = str(datetime.datetime.now().date())
_organizers = ["joey", "chandler", "rachel", "ross"]
print(ev.set_event(_title, _des, _date, _organizers, _images))
# print(ev.get_all_events())