using System;

namespace monit_hackernews.Data
{
    public class NewsHeadline
    {
        public int id { get; set; }

        public int time { get; set; }

        public int score { get; set; }

        public string title { get; set; }

        private string _url;
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
    }
}
