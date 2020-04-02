using System;
using System.Collections.Generic;
using System.Web;

namespace monit_hackernews.Data
{
    public class Item
    {
        // A generic hackernews item
        public int id { get; set; }

        public int time { get; set; }

        public DateTime dateTime
        {
            get
            {
                // convert Unix time to DateTime
                return new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc).
                    AddSeconds(time);
            }
        }

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
            set
            {
                _url = value;
            }
        }
    }

    public class Comment : Item
    {
        // A comment on a news headline
        private string _text;

        public string text
        {
            get 
            {
                return _text;
            }
            set
            {
                _text = HttpUtility.HtmlDecode(value);
            }
        }
    }

    public class NewsHeadline : Item
    {
        // A news headline
        public int score { get; set; }

        public string title { get; set; }

        // comments
        public List<int> kids { get; set; }

        public Comment topComment { get; set; }

        public override string ToString()
        {
            var result = String.Format("{0} {1} {2} {3} {4}", id, dateTime.ToString("f"),
                title, score, url);

            if (!string.IsNullOrEmpty(topComment.text))
            {
                result = String.Format("{0}\n{1}", result, topComment.text);
            }
            return result;
        }
    }
}
