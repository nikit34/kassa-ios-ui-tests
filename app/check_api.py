

class CheckAPI:

    @classmethod
    def check_single_page_url(cls, part_url, line, num_after=0):
        part_line = line.split(part_url, 1)
        if len(part_line) == 2 and part_line[1][:num_after].isdigit():
            return True
        return False

    @classmethod
    def check_general_page_url(cls, part_url, line, params_after=''):
        part_line = line.split(part_url, 1)
        if len(part_line) == 2 and params_after == '' and part_line[1][0] == ';':
            return True
        if len(part_line) == 2 and params_after != '' and part_line[1][0] == '?':
            params_part_line = part_line[1].split(';', 1)
            if isinstance(params_after, list):
                for p in params_after:
                    if p not in params_part_line[0]:
                        return False
                return True
            elif params_after in params_part_line[0]:
                return True
        return False

    @staticmethod
    def _check_images_url(url_part, url_pattern):
        right_url_part = url_part.split(url_pattern)[1]
        if right_url_part.endswith('images'):
            return True
        return False


class HandlersAPI:

    @staticmethod
    def url_creations_movie_filter(msg):
        line = msg['data'].decode('utf-8')
        if CheckAPI.check_single_page_url('/creations/movie/', line, num_after=6):
            url_part, content_part = line.split(';', 5)[3:]
            if CheckAPI._check_images_url(url_part, '/creations/movie/') and '[]' != content_part:
                with open('../../logs/redis_filter.log', 'w') as f:
                    f.write(line)

    @staticmethod
    def url_creations_movie_schedule_filter(msg):
        req_line = msg['data'].decode('utf-8')
        sep_req_line = req_line.split(';', 4)
        if len(sep_req_line) == 5 \
                and sep_req_line[1] == 'response' \
                and sep_req_line[2] == 'GET' \
                and '/creations/movie/' in sep_req_line[3] \
                and '/schedule' in sep_req_line[3]:
            with open('../../logs/redis_filter.log', 'w') as f:
                f.write(req_line)
