using System;

namespace monit_hackernews.Data
{
    public class NewsHeadline
    {
        public int id { get; set; }

        // this needs to match the json result, it is actually unix time
        public int time { get; set; }

        public int score { get; set; }

        public string title { get; set; }

        private string _url;

        public DateTime dateTime
        {
            get
            {
                // convert Unix time to DateTime
                return new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc).
                    AddSeconds(time);
            }
        }
        public string url 
        {
            get 
            {
                if (string.IsNullOrEmpty(_url))
                {
                    _url = String.Format("https://news.ycombinator.com/item?id={0}", id);
                }
                return _url;
            }
            set {
                _url = value;
            }
        }

        public override string ToString()
        {
            return String.Format("{0} {1} {2} {3} {4}", id, dateTime.ToString("f"),
                title, score, url);
        }
    }
}
