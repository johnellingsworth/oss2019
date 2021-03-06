from unittest import TestCase
import frontmatter
from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Files import Files

from oss_hugo.API_Hugo_OSS import API_Hugo_OSS
from oss_hugo.OSS_Participant import OSS_Participant


class test_API_Hugo_OSS(TestCase):

    def setUp(self):
        self.api    = API_Hugo_OSS()
        self.result = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test_df_field(self):
        df   = self.api.df_field('chapter_leader').set_index('title')
        data = df.to_dict()['chapter_leader']
        assert data['Sebastien Deleersnyder'] == 'Belgium'

    def test_md_files_in_folder(self):
        assert len(self.api.md_files_in_folder('content/participant')) > 50

    def test_md_files_participants(self):
        assert len(self.api.md_files_participants()) >50


    def test_participants(self):
        participants = self.api.participants()
        assert len(participants) > 50
        assert set(participants.values().__iter__().__next__()) == {'content', 'path', 'metadata'}


    def test_participants__return_oss_participants(self):
        participants = self.api.participants(return_oss_participants=True)
        assert len(participants) > 50
        assert type(list(participants.values())[0]) == OSS_Participant
        assert 'Dinis Cruz' in set(participants)



    def test_participants_metadatas(self):
        assert len(self.api.participants_metadatas()) > 50

