import sys
import os

stdout = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = stdout
# import all extractors
from spacy_extractors import age_extractor as spacy_age_extractor
from spacy_extractors import social_media_extractor as spacy_social_media_extractor
from spacy_extractors import date_extractor as spacy_date_extractor
from spacy_extractors import address_extractor as spacy_address_extractor
from spacy_extractors import customized_extractor as custom_spacy_extractor
from spacy_extractors import spacy_email_extractor as spacy_email_extractor
from spacy_extractors.default_extractor import DefaultExtractor as default_spacy_extractor
from data_extractors import landmark_extraction
from data_extractors import dictionary_extractor
from data_extractors import regex_extractor
from data_extractors import height_extractor
from data_extractors import weight_extractor
from data_extractors import address_extractor
from data_extractors import age_extractor
from data_extractors import table_extractor
from data_extractors import url_country_extractor
from data_extractors import geonames_extractor
from data_extractors.digPhoneExtractor import phone_extractor
from data_extractors.digEmailExtractor import email_extractor
from data_extractors.digPriceExtractor import price_extractor
from data_extractors.digReviewIDExtractor import review_id_extractor
from data_extractors import date_parser
from classifiers import country_classifier
from structured_extractors import ReadabilityExtractor, TokenizerExtractor, FaithfulTokenizerExtractor
import json
import gzip
import re
import spacy
import codecs
from jsonpath_ng import parse
import time
import collections
import numbers
from tldextract import tldextract
import pickle
import copy
from collections import OrderedDict
import sys
import traceback
import logging
import logstash
import signal
import datetime
import hashlib

_DATA = 'data'
_KEY = 'key'
_VALUE = 'value'
_QUALIFIERS = 'qualifiers'
_KNOWLEDGE_GRAPH = "knowledge_graph"
_EXTRACTION_POLICY = 'extraction_policy'
_KEEP_EXISTING = 'keep_existing'
_REPLACE = 'replace'
_ERROR_HANDLING = 'error_handling'
_IGNORE_EXTRACTION = 'ignore_extraction'
_IGNORE_DOCUMENT = 'ignore_document'
_RAISE_ERROR = 'raise_error'
_CITY_NAME = 'city_name'
_STATE = 'state'
_COUNTRY = 'country'
_CONTENT_EXTRACTION = 'content_extraction'
_SPACY_EXTRACTION = 'spacy_extraction'
_RAW_CONTENT = 'raw_content'
_INPUT_PATH = 'input_path'
_READABILITY = 'readability'
_LANDMARK = 'landmark'
_TITLE = 'title'
_DESCRIPTION = "description"
_INFERLINK_DESCRIPTION = 'inferlink_description'
_STRICT = 'strict'
_FIELD_NAME = 'field_name'
_CONTENT_STRICT = 'content_strict'
_CONTENT_RELAXED = 'content_relaxed'
_YES = 'yes'
_NO = 'no'
_RECALL_PRIORITY = 'recall_priority'
_INFERLINK_EXTRACTIONS = 'inferlink_extractions'
_LANDMARK_THRESHOLD = 'landmark_threshold'
_LANDMARK_RULES = 'landmark_rules'
_URL = 'url'
_AGE = 'age'
_POSTING_DATE = 'posting_date'
_DATE = 'date'
_SOCIAL_MEDIA = 'social_media'
_ADDRESS = 'address'
_EMAIL = "email"
_RESOURCES = 'resources'
_SPACY_FIELD_RULES = "spacy_field_rules"
_DATA_EXTRACTION = 'data_extraction'
_FIELDS = 'fields'
_EXTRACTORS = 'extractors'
_TOKENS = 'tokens'
_TOKENS_ORIGINAL_CASE = "tokens_original_case"
_SIMPLE_TOKENS = 'simple_tokens'
_SIMPLE_TOKENS_ORIGINAL_CASE = 'simple_tokens_original_case'
_TEXT = 'text'
_DICTIONARY = 'dictionary'
_PICKLES = 'pickle'
_NGRAMS = 'ngrams'
_JOINER = 'joiner'
_PRE_FILTER = 'pre_filter'
_POST_FILTER = 'post_filter'
_PRE_PROCESS = "pre_process"
_POST_FILTER_S = "post_filter_s"
_TABLE = "table"
_STOP_WORDS = "stop_words"
_GEONAMES = "geonames"
_STATE_TO_COUNTRY = "state_to_country"
_STATE_TO_CODES_LOWER = "state_to_codes_lower"
_POPULATED_PLACES = "populated_places"
_POPULATED_CITIES = "populated_cities"
_CASE_SENSITIVE = 'case_sensitive'

_EXTRACT_AS_IS = "extract_as_is"
_EXTRACT_USING_DICTIONARY = "extract_using_dictionary"
_EXTRACT_USING_REGEX = "extract_using_regex"
_EXTRACT_FROM_LANDMARK = "extract_from_landmark"
_EXTRACT_PHONE = "extract_phone"
_EXTRACT_EMAIL = "extract_email"
_EXTRACT_PRICE = "extract_price"
_EXTRACT_HEIGHT = "extract_height"
_EXTRACT_WEIGHT = "extract_weight"
_EXTRACT_ADDRESS = "extract_address"
_EXTRACT_AGE = "extract_age"
_CREATE_KG_NODE_EXTRACTOR = "create_kg_node_extractor"
_EXTRACT_WEBSITE_DOMAIN = "extract_website_domain"
_ADD_CONSTANT_KG = "add_constant_kg"
_GUARD = "guard"
_GUARDS = "guards"
_DISABLE_DEFAULT_EXT = "disable_default_extractors"
_STOP_VALUE = 'stop_value'
_MATCH = "match"
_CONTANTS = "constants"

_CONFIG = "config"
_DICTIONARIES = "dictionaries"
_STOP_WORD_DICTIONARIES = "stop_word_dictionaries"
_DECODING_DICTIONARY = "decoding_dictionary"
_INFERLINK = "inferlink"
_HTML = "html"

_SEGMENT_TITLE = "title"
_SEGMENT_INFERLINK_DESC = "inferlink_description"
_SEGMENT_OTHER = "other_segment"
_SEGMENT_NAME = "segment_name"

_METHOD_INFERLINK = "inferlink"

_SOURCE_TYPE = "source_type"
_OBFUSCATION = "obfuscation"

_INCLUDE_CONTEXT = "include_context"
_KG_ENHANCEMENT = "kg_enhancement"
_DOCUMENT_ID = "document_id"
_DOC_ID = 'doc_id'
_TLD = 'tld'
_FEATURE_COMPUTATION = "feature_computation"
_LOGGING = "logging"
_LOGSTASH = "logstash"
_HOST = "host"
_LOCALHOST = "localhost"
_PORT = "port"
_LEVEL = "level"
_VERSION = "version"
_CRITICAL = 50
_ERROR = 40
_WARNING = 30
_INFO = 20
_DEBUG = 10
_EXCEPTION = 47
_ETK_VERSION = "etk_version"
_CONVERT_TO_KG = "convert_to_kg"
_PREFER_INFERLINK_DESCRIPTION = "prefer_inferlink_description"
_TIMEOUT = "timeout"
_JSON_CONTENT = 'json_content'
_PARENT_DOC_ID = 'parent_doc_id'
_FILTERS = 'filters'
_FIELD = 'field'
_REGEX = 'regex'
_ACTION = 'action'
_NO_ACTION = 'no_action'
_KEEP = 'keep'
_DISCARD = 'discard'
_PREFILTER_FILTER_OUTCOME = 'prefilter_filter_outcome'
_CREATED_BY = 'created_by'

remove_break_html_2 = re.compile("[\r\n][\s]*[\r\n]")
remove_break_html_1 = re.compile("[\r\n][\s]*")
remove_break_html_3 = re.compile("(\\n\ *){3,}")
seven_digits = re.compile("[0-9]{7}")


class TimeoutException(Exception):  # Custom exception class
    pass


class InvalidJsonPathException(Exception):
    pass


class Core(object):
    def __init__(self, extraction_config=None, debug=False, load_spacy=False):
        self.extraction_config = extraction_config
        self.debug = debug
        self.html_title_regex = r'<title>(.*?)</title>'
        self.tries = dict()
        self.stop_word_dicts = dict()
        self.pickles = dict()
        self.jobjs = dict()
        self.global_extraction_policy = None
        self.global_error_handling = _RAISE_ERROR
        # to make sure we do not parse json_paths more times than needed, we define the following 2 properties
        self.content_extraction_path = None
        self.data_extraction_path = dict()
        self.kgc_paths = dict()
        self.json_content_paths = dict()
        if load_spacy:
            self.prep_spacy()
            self.prep_origin_spacy()
        else:
            self.nlp = None
            self.origin_nlp = None
        self.country_code_dict = None
        self.matchers = dict()
        self.geonames_dict = None
        self.state_to_country_dict = None
        self.state_to_codes_lower_dict = None
        self.populated_cities = None
        self.logstash_logger = None
        self.etk_version = "1"
        self.prefer_inferlink_description = False
        self.doc_filter_regexes = dict()
        self.guards_path_regex = dict()
        self.readability_timeout = 3
        self.decoding_dict_dict = dict()
        if self.extraction_config:
            if _PREFER_INFERLINK_DESCRIPTION in self.extraction_config:
                self.prefer_inferlink_description = self.extraction_config[_PREFER_INFERLINK_DESCRIPTION]
            self.etk_version = self.extraction_config[_ETK_VERSION] if _ETK_VERSION in self.extraction_config else "1"
            if _LOGGING in self.extraction_config:
                logging_conf = self.extraction_config[_LOGGING]
                if _LOGSTASH in logging_conf:
                    logstash_conf = logging_conf[_LOGSTASH]
                    self.logstash_logger = logging.getLogger('etk-logstash-logger')
                    host = logstash_conf[_HOST] if _HOST in logstash_conf else _LOCALHOST
                    port = logstash_conf[_PORT] if _PORT in logstash_conf else 5959
                    self.logstash_logger.setLevel(logstash_conf[_LEVEL] if _LEVEL in logstash_conf else _ERROR)
                    self.logstash_logger.addHandler(
                        logstash.LogstashHandler(host, port,
                                                 logstash_conf[_VERSION] if _VERSION in logging_conf else 1))

            """
            load the decoding dictionaries.
            because this will be used as post filter, we'll load any decoding dictionary here
             """
            if _RESOURCES in self.extraction_config and _DECODING_DICTIONARY in self.extraction_config[_RESOURCES]:
                decoding_dict = self.extraction_config[_RESOURCES][_DECODING_DICTIONARY]
                for key in decoding_dict.keys():
                    self.decoding_dict_dict[key] = self.process_decoding_dict(self.load_json_file(decoding_dict[key]))

    def log(self, message, level, doc_id=None, url=None, extra=None):
        if self.logstash_logger:
            if not extra:
                extra = dict()
            extra[_ETK_VERSION] = self.etk_version
            if doc_id:
                extra[_DOCUMENT_ID] = doc_id
            if url:
                extra[_URL] = url

            if level == _ERROR:
                self.logstash_logger.error(message, extra=extra)
            elif level == _WARNING:
                self.logstash_logger.warning(message, extra=extra)
            elif level == _INFO:
                self.logstash_logger.info(message, extra=extra)
            elif level == _DEBUG:
                self.logstash_logger.debug(message, extra=extra)
            elif level == _CRITICAL:
                self.logstash_logger.critical(message, extra=extra)
            elif level == _EXCEPTION:
                self.logstash_logger.exception(message, extra=extra)

    """ Define all API methods """

    @staticmethod
    def timeout_handler(signum, frame):  # Custom signal handler
        raise TimeoutException

    def process_doc_filters(self, doc):
        if self.extraction_config:
            if _FILTERS in self.extraction_config:
                filters = self.extraction_config[_FILTERS]
                if _URL in doc:
                    if _TLD not in doc:
                        doc[_TLD] = self.extract_tld(doc[_URL])
                    tld = doc[_TLD]
                    if tld in filters:
                        doc_filters = filters[tld]

                        if not isinstance(doc_filters, list):
                            doc_filters = [doc_filters]
                        for doc_filter in doc_filters:
                            if _FIELD in doc_filter and _ACTION in doc_filter and _REGEX in doc_filter:
                                field = doc_filter[_FIELD]
                                action = doc_filter[_ACTION]
                                regex = doc_filter[_REGEX]
                                if action.lower() not in [_NO_ACTION, _KEEP, _DISCARD]:
                                    print
                                    'action: {} in filters is not one of {}, {} or {}. Defaulting to {}'.format(
                                        action, _NO_ACTION, _KEEP, _DISCARD, _NO_ACTION)
                                    action = _NO_ACTION

                                if field in doc:
                                    if isinstance(doc[field], basestring):
                                        if regex not in self.doc_filter_regexes:
                                            self.doc_filter_regexes[regex] = re.compile(regex)
                                        regex_c = self.doc_filter_regexes[regex]
                                        match = regex_c.search(doc[field])
                                        if match:
                                            doc[_PREFILTER_FILTER_OUTCOME] = action
                                            break
                                    else:
                                        print
                                        'Error while filtering out docs: field - {} is not a literal in ' \
                                        'the doc.'.format(field)
                            else:
                                message = 'Incomplete filter: {} for tld: {} in etk config'.format(doc_filter, tld)
                                print
                                message
                                self.log(message, _INFO)
        # if for some reason, there is no action defined: no_action is default action
        if _PREFILTER_FILTER_OUTCOME not in doc:
            doc[_PREFILTER_FILTER_OUTCOME] = _NO_ACTION
        return doc

    def process(self, doc, create_knowledge_graph=True, html_description=False):
        start_time_process = time.time()
        try:
            if self.extraction_config:
                doc_id = None
                if _DOCUMENT_ID in self.extraction_config:
                    doc_id_field = self.extraction_config[_DOCUMENT_ID]
                    if doc_id_field in doc:
                        doc_id = doc[doc_id_field]
                        doc[_DOCUMENT_ID] = doc_id
                        # TODO this is a hack, remove this later
                        if 'doc_id' not in doc:
                            doc['doc_id'] = doc_id
                    else:
                        raise KeyError('{} not found in the input document'.format(doc_id_field))

                if _EXTRACTION_POLICY in self.extraction_config:
                    self.global_extraction_policy = self.extraction_config[_EXTRACTION_POLICY]
                error_handling = self.extraction_config[
                    _ERROR_HANDLING] if _ERROR_HANDLING in self.extraction_config else _RAISE_ERROR
                if error_handling != _RAISE_ERROR and error_handling != _IGNORE_DOCUMENT:
                    warning = 'WARN: error handling in extraction config can either be \"{}\" or \"{}\".' \
                              ' By default its value has been set to \"{}\"'.format(
                        _RAISE_ERROR, _IGNORE_DOCUMENT, _RAISE_ERROR)
                    self.log(warning, _WARNING)
                    error_handling = _RAISE_ERROR
                self.global_error_handling = error_handling

                # Before we process the doc, run filter docs
                doc = self.process_doc_filters(doc)
                if doc[_PREFILTER_FILTER_OUTCOME] == _DISCARD:
                    return None

                """Handle content extraction first aka Phase 1"""
                if _CONTENT_EXTRACTION in self.extraction_config:
                    if _CONTENT_EXTRACTION not in doc:
                        doc[_CONTENT_EXTRACTION] = dict()
                    ce_config = self.extraction_config[_CONTENT_EXTRACTION]
                    content_extraction_guards = ce_config[_GUARDS] if _GUARDS in ce_config else None

                    # JSON CONTENT: create content for data extraction from json paths
                    if _JSON_CONTENT in ce_config:
                        jc_extractors = ce_config[_JSON_CONTENT]
                        if isinstance(jc_extractors, dict):
                            jc_extractors = [jc_extractors]
                        for jc_extractor in jc_extractors:
                            doc = self.convert_json_content(doc, jc_extractor)

                    html_path = ce_config[_INPUT_PATH] if _INPUT_PATH in ce_config else None
                    if not html_path and _EXTRACTORS in ce_config:
                        raise KeyError('{} not found in extraction_config'.format(_INPUT_PATH))
                    if html_path and _EXTRACTORS in ce_config:
                        if not self.content_extraction_path:
                            try:
                                self.content_extraction_path = parse(html_path)
                            except:
                                raise InvalidJsonPathException(
                                    '\'{}\' is not a valid json path'.format(html_path))
                        matches = self.content_extraction_path.find(doc)

                        extractors = ce_config[_EXTRACTORS]

                        run_readability = True
                        for index in range(len(matches)):
                            for extractor in extractors.keys():
                                if content_extraction_guards and not self.assert_data_extraction_guard(
                                        content_extraction_guards, doc, matches[index].value):
                                    continue
                                if extractor == _LANDMARK:
                                    doc[_CONTENT_EXTRACTION] = self.run_landmark(doc[_CONTENT_EXTRACTION],
                                                                                 matches[index].value,
                                                                                 extractors[extractor], doc[_URL])

                                    landmark_config = extractors[extractor]
                                    landmark_field_name = landmark_config[_FIELD_NAME] if _FIELD_NAME in landmark_config \
                                        else _INFERLINK_EXTRACTIONS
                                    if self.prefer_inferlink_description:
                                        if landmark_field_name in doc[_CONTENT_EXTRACTION]:
                                            if _INFERLINK_DESCRIPTION in doc[_CONTENT_EXTRACTION][landmark_field_name]:
                                                inferlink_desc = doc[_CONTENT_EXTRACTION][landmark_field_name][
                                                    _INFERLINK_DESCRIPTION]
                                                if _TEXT in inferlink_desc and inferlink_desc[_TEXT] and inferlink_desc[
                                                    _TEXT].strip() != '':
                                                    run_readability = False

                                elif extractor == _READABILITY:
                                    if 'crawler' in doc and doc['crawler'] == 'Sage-LexisNexis-Crawler':
                                        run_readability = False
                                    if run_readability:
                                        re_extractors = extractors[extractor]
                                        if isinstance(re_extractors, dict):
                                            re_extractors = [re_extractors]

                                        for re_extractor in re_extractors:
                                            doc[_CONTENT_EXTRACTION] = self.run_readability(doc[_CONTENT_EXTRACTION],
                                                                                            matches[index].value,
                                                                                            re_extractor)
                                elif extractor == _TITLE:
                                    doc[_CONTENT_EXTRACTION] = self.run_title(doc[_CONTENT_EXTRACTION],
                                                                              matches[index].value,
                                                                              extractors[extractor])

                                elif extractor == _TABLE:
                                    doc[_CONTENT_EXTRACTION] = self.run_table_extractor(doc[_CONTENT_EXTRACTION],
                                                                                        matches[index].value,
                                                                                        extractors[extractor])

                    # Add the url as segment as well
                    if _URL in doc and doc[_URL] and doc[_URL].strip() != '':
                        doc[_CONTENT_EXTRACTION][_URL] = dict()
                        doc[_CONTENT_EXTRACTION][_URL][_TEXT] = doc[_URL]
                        if _TLD not in doc:
                            doc[_TLD] = self.extract_tld(doc[_URL])

                """Phase 2: The Data Extraction"""
                if _DATA_EXTRACTION in self.extraction_config:
                    de_configs = self.extraction_config[_DATA_EXTRACTION]
                    if isinstance(de_configs, dict):
                        de_configs = [de_configs]

                    for i in range(len(de_configs)):
                        de_config = de_configs[i]
                        input_paths = de_config[_INPUT_PATH] if _INPUT_PATH in de_config else None
                        if not input_paths:
                            raise KeyError('{} not found for data extraction in extraction_config'.format(_INPUT_PATH))

                        if not isinstance(input_paths, list):
                            input_paths = [input_paths]
                        # get user defined guards
                        guards = de_config[_GUARDS] if _GUARDS in de_config else None
                        for input_path in input_paths:
                            if _FIELDS in de_config:
                                if input_path not in self.data_extraction_path:
                                    try:
                                        self.data_extraction_path[input_path] = parse(input_path)
                                    except:
                                        raise InvalidJsonPathException(
                                            '\'{}\' is not a valid json path'.format(input_path))
                                matches = self.data_extraction_path[input_path].find(doc)
                                for match in matches:
                                    if guards and not self.assert_data_extraction_guard(guards, doc, match.value):
                                        continue
                                    # First rule of DATA Extraction club: Get tokens
                                    # Get the crf tokens
                                    if _TEXT in match.value:
                                        cleaned_text = self.remove_line_breaks(match.value[_TEXT])
                                        match.value[_TEXT] = cleaned_text
                                        if _SIMPLE_TOKENS_ORIGINAL_CASE not in match.value:
                                            match.value[_SIMPLE_TOKENS_ORIGINAL_CASE] = self.extract_crftokens(
                                                match.value[_TEXT],
                                                lowercase=False, create_structured_tokens=False)
                                        if _SIMPLE_TOKENS not in match.value:
                                            match.value[_SIMPLE_TOKENS] = [val.lower() for val in
                                                                           match.value[_SIMPLE_TOKENS_ORIGINAL_CASE]]

                                    fields = de_config[_FIELDS]
                                    for field in fields.keys():
                                        run_extractor = True
                                        full_path = str(match.full_path)
                                        segment = self.determine_segment(full_path)
                                        if field != '*':
                                            if run_extractor:
                                                if _EXTRACTORS in fields[field]:
                                                    extractors = fields[field][_EXTRACTORS]
                                                    for extractor in extractors.keys():
                                                        try:
                                                            foo = getattr(self, extractor)
                                                        except:
                                                            foo = None
                                                        if foo:
                                                            # score is 1.0 because every method thinks it is the best
                                                            score = 1.0
                                                            method = extractor
                                                            if _CONFIG not in extractors[extractor]:
                                                                extractors[extractor][_CONFIG] = dict()
                                                            extractors[extractor][_CONFIG][_FIELD_NAME] = field
                                                            ep = self.determine_extraction_policy(extractors[extractor])
                                                            if extractor == _CREATE_KG_NODE_EXTRACTOR:
                                                                method = _CREATE_KG_NODE_EXTRACTOR
                                                                segment = str(match.full_path)
                                                                results = self.create_kg_node_extractor(match.value,
                                                                                                        extractors[
                                                                                                            extractor][
                                                                                                            _CONFIG],
                                                                                                        doc, doc_id,
                                                                                                        url=doc[
                                                                                                            _URL] if
                                                                                                        _URL in doc
                                                                                                        else None)
                                                                if results:
                                                                    results = self.add_origin_info(
                                                                        results, method,
                                                                        segment,
                                                                        score,
                                                                        doc_id)
                                                                    if create_knowledge_graph:
                                                                        self.create_knowledge_graph(doc,
                                                                                                    field,
                                                                                                    results)
                                                            elif extractor == _EXTRACT_FROM_LANDMARK:
                                                                if _FIELDS in extractors[extractor][_CONFIG]:
                                                                    inferlink_fields = extractors[extractor][_CONFIG][
                                                                        _FIELDS]
                                                                    for inferlink_field in inferlink_fields:
                                                                        if _INFERLINK_EXTRACTIONS in full_path and inferlink_field in full_path:
                                                                            method = _METHOD_INFERLINK
                                                                            if self.check_if_run_extraction(match.value,
                                                                                                            field,
                                                                                                            extractor,
                                                                                                            ep):
                                                                                results = foo(doc,
                                                                                              extractors[extractor][
                                                                                                  _CONFIG],
                                                                                              selected_field=inferlink_field)
                                                                                if results:
                                                                                    results = self.add_origin_info(
                                                                                        results, method,
                                                                                        segment,
                                                                                        score,
                                                                                        doc_id)
                                                                                    if create_knowledge_graph:
                                                                                        self.create_knowledge_graph(doc,
                                                                                                                    field,
                                                                                                                    results)
                                                                else:
                                                                    if _INFERLINK_EXTRACTIONS in full_path and field in full_path:
                                                                        method = _METHOD_INFERLINK
                                                                        if self.check_if_run_extraction(match.value,
                                                                                                        field,
                                                                                                        extractor,
                                                                                                        ep):

                                                                            results = foo(doc,
                                                                                          extractors[extractor][
                                                                                              _CONFIG])
                                                                            if results:
                                                                                results = self.add_origin_info(
                                                                                    results,
                                                                                    method,
                                                                                    segment,
                                                                                    score,
                                                                                    doc_id)
                                                                                if create_knowledge_graph:
                                                                                    self.create_knowledge_graph(doc,
                                                                                                                field,
                                                                                                                results)
                                                            else:
                                                                if extractor == _EXTRACT_WEBSITE_DOMAIN:
                                                                    if _TLD in doc:
                                                                        extractors[extractor][_CONFIG][_TLD] = doc[_TLD]
                                                                if extractor == _EXTRACT_AS_IS:
                                                                    segment = str(match.full_path)
                                                                else:
                                                                    segment = self.determine_segment(full_path)
                                                                if self.check_if_run_extraction(match.value, field,
                                                                                                extractor,
                                                                                                ep):
                                                                    results = foo(match.value,
                                                                                  extractors[extractor][_CONFIG])
                                                                    if results:
                                                                        results = self.add_origin_info(
                                                                            results,
                                                                            method,
                                                                            segment,
                                                                            score,
                                                                            doc_id)
                                                                        if create_knowledge_graph:
                                                                            self.create_knowledge_graph(doc, field,
                                                                                                        results)
                                        else:  # extract whatever you can!
                                            if _EXTRACTORS in fields[field]:
                                                extractors = fields[field][_EXTRACTORS]
                                                for extractor in extractors.keys():
                                                    try:
                                                        foo = getattr(self, extractor)
                                                    except Exception as e:
                                                        foo = None
                                                    if foo:
                                                        # score is 1.0 because every method thinks it is the best
                                                        score = 1.0
                                                        method = extractor
                                                        if _CONFIG not in extractors[extractor]:
                                                            extractors[extractor][_CONFIG] = dict()
                                                        ep = self.determine_extraction_policy(extractors[extractor])
                                                        if extractor == _EXTRACT_FROM_LANDMARK:
                                                            if _INFERLINK_EXTRACTIONS in full_path and field in full_path:
                                                                method = _METHOD_INFERLINK
                                                                if self.check_if_run_extraction(match.value, field,
                                                                                                extractor,
                                                                                                ep):

                                                                    results = foo(doc, extractors[extractor][_CONFIG])
                                                                    if results:
                                                                        results = self.add_origin_info(results,
                                                                                                       method,
                                                                                                       segment,
                                                                                                       score,
                                                                                                       doc_id)
                                                                        if create_knowledge_graph:
                                                                            self.create_knowledge_graph(doc, field,
                                                                                                        results)
                                                        else:
                                                            results = foo(match.value,
                                                                          extractors[extractor][_CONFIG])
                                                            if results:
                                                                for f, res in results.items():
                                                                    res = self.add_origin_info(res,
                                                                                               method,
                                                                                               segment,
                                                                                               score, doc_id)
                                                                    if create_knowledge_graph:
                                                                        self.create_knowledge_graph(doc, f, res)
                                                    else:
                                                        self.log('method {} not found!'.format(extractor), _INFO)

                """Optional Phase 3: Knowledge Graph Enhancement"""
                if _KG_ENHANCEMENT in self.extraction_config:
                    kg_configs = self.extraction_config[_KG_ENHANCEMENT]
                    if isinstance(kg_configs, dict):
                        kg_configs = [kg_configs]

                    for i in range(len(kg_configs)):
                        kg_config = kg_configs[i]
                        input_paths = kg_config[_INPUT_PATH] if _INPUT_PATH in kg_config else None
                        if not input_paths:
                            raise KeyError(
                                '{} not found for knowledge graph enhancement in extraction_config'.format(_INPUT_PATH))

                        if not isinstance(input_paths, list):
                            input_paths = [input_paths]

                        for input_path in input_paths:
                            if _FIELDS in kg_config:
                                if input_path not in self.data_extraction_path:
                                    try:
                                        self.data_extraction_path[input_path] = parse(input_path)
                                    except:
                                        raise InvalidJsonPathException(
                                            '\'{}\' is not a valid json path'.format(input_path))
                                matches = self.data_extraction_path[input_path].find(doc)
                                for match in matches:
                                    fields = kg_config[_FIELDS]
                                    try:
                                        sorted_fields = self.sort_dictionary_by_fields(fields)
                                    except:
                                        raise ValueError('Please ensure there is a priority added to every field in '
                                                         'knowledge_graph  enhancement and the priority is a number')

                                    for i in range(0, len(sorted_fields)):
                                        field = sorted_fields[i][0]
                                        guard_result = True
                                        if _GUARD in fields[field]:
                                            guard_result = self.process_kg_enchancement_guards(doc,
                                                                                               fields[field][_GUARD])
                                        if guard_result:
                                            if _EXTRACTORS in fields[field]:
                                                extractors = fields[field][_EXTRACTORS]
                                                for extractor in extractors.keys():
                                                    try:
                                                        foo = getattr(self, extractor)
                                                    except:
                                                        foo = None
                                                    if foo:
                                                        if _CONFIG not in extractors[extractor]:
                                                            extractors[extractor][_CONFIG] = dict()
                                                        extractors[extractor][_CONFIG][_FIELD_NAME] = field
                                                        results = foo(match.value, extractors[extractor][_CONFIG])
                                                        if results:
                                                            if not extractor == 'filter_results':
                                                                if extractor == _ADD_CONSTANT_KG:
                                                                    # add origin info
                                                                    results = self.add_origin_info(results,
                                                                                                   extractor,
                                                                                                   _KG_ENHANCEMENT,
                                                                                                   1.0, doc_id)
                                                                self.create_knowledge_graph(doc, field, results)

                if _KNOWLEDGE_GRAPH in doc and doc[_KNOWLEDGE_GRAPH]:
                    """ Add title and description as fields in the knowledge graph as well"""
                    doc = Core.rearrange_description(doc, html_description)
                    doc = Core.rearrange_title(doc)

        except InvalidJsonPathException as e:
            raise e
        except Exception as e:
            self.log('ETK process() Exception', _EXCEPTION, doc_id=doc[_DOCUMENT_ID],
                     url=doc[_URL] if _URL in doc else None)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            print
            ''.join(lines)
            if self.global_error_handling == _RAISE_ERROR:
                raise e
            else:
                return None
        end_time_process = time.time()
        time_taken_process = end_time_process - start_time_process
        if '@execution_profile' not in doc:
            doc['@execution_profile'] = dict()
        doc['@execution_profile']['@etk_start_time'] = datetime.datetime.utcfromtimestamp(
            start_time_process).isoformat()
        doc['@execution_profile']['@etk_end_time'] = datetime.datetime.utcfromtimestamp(end_time_process).isoformat()
        doc['@execution_profile']['@etk_process_time'] = float(end_time_process - start_time_process)
        if time_taken_process > 5:
            extra = dict()
            extra['time_taken'] = time_taken_process
            print
            'LOG: {},{},{},{}'.format(doc_id, 'TOTAL', 'TOTAL', time_taken_process)
            self.log('Document: {} took {} seconds'.format(doc[_DOCUMENT_ID], str(time_taken_process)), _INFO,
                     doc_id=doc[_DOCUMENT_ID], url=doc[_URL] if _URL in doc else None, extra=extra)
        return doc

    def process_kg_enchancement_guards(self, doc, guards):
        if _KNOWLEDGE_GRAPH not in doc:
            return False

        if not isinstance(guards, list):
            guards = [guards]

        result = True
        for guard in guards:
            if _FIELD in guard:
                g_field = guard[_FIELD]
                if g_field in doc[_KNOWLEDGE_GRAPH]:
                    kg_values = doc[_KNOWLEDGE_GRAPH][g_field] if g_field in doc[_KNOWLEDGE_GRAPH] else None
                    if not kg_values:
                        return False

                    match_field = guard[_MATCH] if _MATCH in guard else _VALUE
                    try:
                        values = [v[match_field] for v in kg_values]
                    except:
                        values = [v[_VALUE] for v in kg_values]
                    result &= self.process_one_guard(values, guard)
                elif g_field in doc:
                    result &= self.process_one_guard(doc[g_field], guard)
                else:
                    return False
            if not result:
                break
        return result

    def process_one_guard(self, lista, guard):
        if not isinstance(lista, list):
            lista = [lista]
        if _REGEX in guard:
            regex = guard[_REGEX]
            if regex not in self.doc_filter_regexes:
                self.doc_filter_regexes[regex] = re.compile(regex)
            regex_c = self.doc_filter_regexes[regex]
            for val in lista:
                match = regex_c.search(val)
                if match:
                    return True
        if _VALUE in guard:
            listb = guard[_VALUE] if isinstance(guard[_VALUE], list) else [guard[_VALUE]]
            return Core.do_lists_intersect(lista, listb)
        if _STOP_VALUE in guard:
            listb = guard[_STOP_VALUE] if isinstance(guard[_STOP_VALUE], list) else [guard[_STOP_VALUE]]
            return not Core.do_lists_intersect(lista, listb)

        return False

    @staticmethod
    def do_lists_intersect(lista, listb):
        # the following if statement is redundant, its there because of consistent return of function
        return True if set(lista) & set(listb) else False

    def convert_json_content(self, doc, json_content_extractor):
        input_path = json_content_extractor[_INPUT_PATH]
        segment_name = json_content_extractor[_SEGMENT_NAME]
        val_list = list()

        if input_path not in self.json_content_paths:
            try:
                self.json_content_paths[input_path] = parse(input_path)
            except Exception as e:
                raise InvalidJsonPathException(
                    '\'{}\' is not a valid json path'.format(input_path))
        matches = self.json_content_paths[input_path].find(doc)
        for match in matches:
            values = match.value
            if not isinstance(values, list):
                values = [values]
            for val in values:
                if isinstance(val, basestring) or isinstance(val, numbers.Number):
                    o = dict()
                    o[_TEXT] = unicode(val)
                    val_list.append(o)
                elif isinstance(val, dict):
                    if _VALUE in val:
                        o = dict()
                        o[_TEXT] = val[_VALUE]
                        if _KEY in val:
                            o[_KEY] = val[_KEY]
                        if _QUALIFIERS in val:
                            o[_QUALIFIERS] = val[_QUALIFIERS]
                        val_list.append(o)
                else:
                    if val:
                        msg = 'Error while extracting json content, input path: {} is either not a leaf node in ' \
                              'the json or not a dict with keys \'value\', \'key\' and/or \'qualifiers\'  ' \
                              'document'.format(input_path)
                        self.log(msg, _ERROR)
                        print
                        msg
                        if self.global_error_handling == _RAISE_ERROR:
                            raise ValueError(msg)
        if len(val_list) > 0:
            if _CONTENT_EXTRACTION not in doc:
                doc[_CONTENT_EXTRACTION] = dict()
            if segment_name not in doc[_CONTENT_EXTRACTION]:
                doc[_CONTENT_EXTRACTION][segment_name] = list()
            doc[_CONTENT_EXTRACTION][segment_name].extend(val_list)
        return doc

    def extract_as_is(self, d, config=None):
        if isinstance(d, basestring):
            result = self.pseudo_extraction_results(d)
            if config and _POST_FILTER in config:
                post_filters = config[_POST_FILTER]
                result = self.run_post_filters_results(result, post_filters, field_name=config[_FIELD_NAME])

            return result

        elif isinstance(d, dict) and _TEXT in d:
            if d[_TEXT].strip() != '':
                result = self.pseudo_extraction_results(d[_TEXT], key=d[_KEY] if _KEY in d else None,
                                                        qualifiers=d[_QUALIFIERS] if _QUALIFIERS in d else None)
                if config and _POST_FILTER in config:
                    post_filters = config[_POST_FILTER]
                    result = self.run_post_filters_results(result, post_filters, field_name=config[_FIELD_NAME])
                return self._relevant_text_from_context(d[_TEXT], result, config[_FIELD_NAME])
            else:
                return None

        # this is the case where we are going to put the input object to a field called 'data'
        elif isinstance(d, dict) or isinstance(d, list):
            str_d = json.dumps(d, sort_keys=True)
            key = hashlib.sha256(str_d).hexdigest().upper()
            result = self.pseudo_extraction_results(str_d, key=key)
            result[_DATA] = d
            return result
        # If nothing matches,
        return None

    @staticmethod
    def pseudo_extraction_results(value, key=None, qualifiers=None):
        result = dict()
        result[_VALUE] = value
        if key:
            result[_KEY] = key
        if qualifiers:
            result[_QUALIFIERS] = qualifiers
        return result

    @staticmethod
    def remove_line_breaks(x):
        try:
            # x_1 = re.sub(remove_break_html_1, ' \n ', x)
            # x_2 = re.sub(remove_break_html_2, ' \n\n ', x_1)
            x_2 = re.sub(remove_break_html_3, ' \n\n ', x)
            x_2 = x_2.replace('\n', '<br/>')
        except:
            return x
        return x_2

    @staticmethod
    def rearrange_description(doc, html_description=False):
        method = 'rearrange_description'
        description = None
        segment = ''
        if _CONTENT_EXTRACTION in doc:
            ce = doc[_CONTENT_EXTRACTION]
            if _INFERLINK_EXTRACTIONS in ce:
                if _INFERLINK_DESCRIPTION in ce[_INFERLINK_EXTRACTIONS]:
                    description = ce[_INFERLINK_EXTRACTIONS][_INFERLINK_DESCRIPTION][_TEXT]
                    segment = _INFERLINK
                elif _CONTENT_RELAXED in ce:
                    description = ce[_CONTENT_RELAXED][_TEXT]
                    segment = _CONTENT_RELAXED

            if not description or description.strip() == '':
                if _CONTENT_STRICT in ce:
                    description = ce[_CONTENT_STRICT][_TEXT]
                    segment = _CONTENT_STRICT

            if description and description != '':
                if html_description:
                    description = Core.remove_line_breaks(description)
                if _KNOWLEDGE_GRAPH not in doc:
                    doc[_KNOWLEDGE_GRAPH] = dict()
                if _DESCRIPTION not in doc[_KNOWLEDGE_GRAPH]:
                    doc[_KNOWLEDGE_GRAPH][_DESCRIPTION] = list()
                    o = dict()
                    o['value'] = description
                    o['key'] = 'description'
                    o['confidence'] = 1
                    o['provenance'] = [Core.custom_provenance_object(method, segment, doc[_DOCUMENT_ID])]
                    doc[_KNOWLEDGE_GRAPH][_DESCRIPTION].append(o)
        return doc

    @staticmethod
    def sort_dictionary_by_fields(dictionary):
        sorted_d = OrderedDict(sorted(dictionary.iteritems(), key=lambda x: x[1]['priority']))
        return sorted_d.items()

    @staticmethod
    def custom_provenance_object(method, segment, document_id):
        prov = dict()
        prov['method'] = method
        prov['source'] = dict()
        prov['source']['segment'] = segment
        prov['source'][_DOCUMENT_ID] = document_id
        return prov

    @staticmethod
    def rearrange_title(doc):
        method = 'rearrange_title'
        title = None
        segment = ''
        if _CONTENT_EXTRACTION in doc:
            ce = doc[_CONTENT_EXTRACTION]
            if _INFERLINK_EXTRACTIONS in ce:
                if _TITLE in ce[_INFERLINK_EXTRACTIONS]:
                    title = ce[_INFERLINK_EXTRACTIONS][_TITLE][_TEXT]
                    segment = _INFERLINK
            if not title or title.strip() == '':
                if _TITLE in ce:
                    title = ce[_TITLE][_TEXT]
                    segment = _HTML
            if not title or title.strip() == '':
                if _CONTENT_RELAXED in ce:
                    vals = ce[_CONTENT_RELAXED][_TEXT].split(' ')
                    new_vals = list()
                    for i in range(0, len(vals)):
                        if len(new_vals) == 10:
                            break
                        if vals[i].strip() != '':
                            new_vals.append(vals[i])
                    title = ' '.join(new_vals)
                    segment = _HTML

            if title and title != '':
                if _KNOWLEDGE_GRAPH not in doc:
                    doc[_KNOWLEDGE_GRAPH] = dict()
                if _TITLE not in doc[_KNOWLEDGE_GRAPH]:
                    doc[_KNOWLEDGE_GRAPH][_TITLE] = list()
                    o = dict()
                    o['value'] = title
                    o['key'] = 'title'
                    o['confidence'] = 1
                    o['provenance'] = [Core.custom_provenance_object(method, segment, doc[_DOCUMENT_ID])]
                    doc[_KNOWLEDGE_GRAPH][_TITLE].append(o)

        return doc

    @staticmethod
    def extract_tld(url):
        return tldextract.extract(url).domain + '.' + tldextract.extract(url).suffix

    @staticmethod
    def create_knowledge_graph(doc, field_name, extractions):
        if _KNOWLEDGE_GRAPH not in doc:
            doc[_KNOWLEDGE_GRAPH] = dict()

        if field_name not in doc[_KNOWLEDGE_GRAPH]:
            doc[_KNOWLEDGE_GRAPH][field_name] = list()

        for extraction in extractions:
            if 'key' in extraction:
                key = extraction['key']
            else:
                key = extraction['value']
                if (isinstance(key, basestring) or isinstance(key, numbers.Number)) and field_name != _POSTING_DATE:
                    # try except block because unicode characters will not be lowered
                    try:
                        key = str(key).strip().lower()
                    except:
                        pass
                if 'metadata' in extraction:
                    sorted_metadata = Core.sort_dict(extraction['metadata'])
                    for k, v in sorted_metadata.iteritems():
                        if isinstance(v, numbers.Number):
                            v = str(v)
                        # if v:
                        #     v = v.encode('utf-8')
                        if v and v.strip() != '':
                            # key += '-' + str(k) + ':' + str(v)
                            key = '{}-{}:{}'.format(key, k, v)

            # TODO FIX THIS HACK
            if len(key) > 32766:
                key = key[0:500]

            provenance = dict()
            method = None
            confidence = None
            metadata = None
            value = None

            if 'origin' in extraction:
                origin = extraction['origin']
                if 'obfuscation' in extraction:
                    origin['extraction_metadata'] = dict()
                    origin['extraction_metadata']['obfuscation'] = extraction['obfuscation']
                method = origin['method']
                confidence = origin['score']
                origin.pop('score', None)
                origin.pop('method', None)
                provenance['source'] = origin

            if 'context' in extraction:
                provenance['source']['context'] = extraction['context']
            if 'metadata' in extraction and not metadata:
                metadata = extraction['metadata']
            if method:
                provenance["method"] = method
            if not value:
                value = extraction['value']
                provenance['extracted_value'] = value
            if confidence:
                provenance['confidence'] = dict()
                provenance['confidence']['extraction'] = confidence
            if metadata:
                provenance['qualifiers'] = metadata
            doc[_KNOWLEDGE_GRAPH][field_name] = Core.add_extraction_knowledge_graph(
                doc[_KNOWLEDGE_GRAPH][field_name], provenance, key, value, confidence if confidence else 1,
                data=extraction[_DATA] if _DATA in extraction else None)

        return doc

    @staticmethod
    def add_extraction_knowledge_graph(kg_extractions, provenance, key, value, confidence=1, data=None):
        if len(kg_extractions) > 0:
            for kg_e in kg_extractions:
                if key == kg_e['key']:
                    kg_e['provenance'].append(provenance)
                    return kg_extractions

        kg_extraction = dict()
        kg_extraction['provenance'] = [provenance]
        kg_extraction['value'] = value
        kg_extraction['key'] = key
        kg_extraction['confidence'] = confidence
        if data:
            kg_extraction[_DATA] = data
        kg_extractions.append(kg_extraction)
        return kg_extractions

    @staticmethod
    def add_data_extraction_results(d, field_name, method_name, results):
        if _DATA_EXTRACTION not in d:
            d[_DATA_EXTRACTION] = dict()
        if field_name not in d[_DATA_EXTRACTION]:
            d[_DATA_EXTRACTION][field_name] = dict()
        if method_name not in d[_DATA_EXTRACTION][field_name]:
            d[_DATA_EXTRACTION][field_name][method_name] = dict()
        if isinstance(results, dict):
            results = [results]
        if 'results' not in d[_DATA_EXTRACTION][field_name][method_name]:
            d[_DATA_EXTRACTION][field_name][method_name]['results'] = results
        else:
            d[_DATA_EXTRACTION][field_name][method_name]['results'].extend(results)
        return d

    @staticmethod
    def check_if_run_extraction(d, field_name, method_name, extraction_policy):
        try:  # do not run anything over 1 MB
            if _TEXT in d and len(d[_TEXT]) > 1000000:
                return False
        except:
            pass
        if _DATA_EXTRACTION not in d:
            return True
        if field_name not in d[_DATA_EXTRACTION]:
            return True
        if method_name not in d[_DATA_EXTRACTION][field_name]:
            return True
        if 'results' not in d[_DATA_EXTRACTION][field_name][method_name]:
            return True
        else:
            if extraction_policy == _REPLACE:
                return True
        return False

    @staticmethod
    def determine_segment(json_path):
        segment = _SEGMENT_OTHER
        if _SEGMENT_INFERLINK_DESC in json_path:
            segment = _SEGMENT_INFERLINK_DESC
        elif _INFERLINK in json_path and _SEGMENT_INFERLINK_DESC not in json_path:
            segment = _HTML
        elif _CONTENT_STRICT in json_path:
            segment = _CONTENT_STRICT
        elif _CONTENT_RELAXED in json_path:
            segment = _CONTENT_RELAXED
        elif _TITLE in json_path:
            segment = _TITLE
        elif _URL in json_path:
            segment = _URL
        return segment

    @staticmethod
    def add_origin_info(results, method, segment, score, doc_id=None):
        if results:
            if not isinstance(results, list):
                results = [results]
            for result in results:
                o = dict()
                o['segment'] = segment
                o['method'] = method
                o['score'] = score
                if doc_id:
                    o[_DOCUMENT_ID] = doc_id
                result['origin'] = o
        return results

    def run_landmark(self, content_extraction, html, landmark_config, url):
        field_name = landmark_config[_FIELD_NAME] if _FIELD_NAME in landmark_config else _INFERLINK_EXTRACTIONS
        ep = self.determine_extraction_policy(landmark_config)
        extraction_rules = self.consolidate_landmark_rules()
        if _LANDMARK_THRESHOLD in landmark_config:
            pct = landmark_config[_LANDMARK_THRESHOLD]
            if not 0.0 <= pct <= 1.0:
                raise ValueError('landmark threshold should be a float between {} and {}'.format(0.0, 1.0))
        else:
            pct = 0.5
        if field_name not in content_extraction or (field_name in content_extraction and ep == _REPLACE):
            ifl_extractions = Core.extract_landmark(html, url, extraction_rules, pct)

            if isinstance(ifl_extractions, list):
                # we have a rogue post type page, put it in its place
                # Change Oct 5, 2017: Since we are not showing threads, pick the first post and extract from it
                # preserve the original posts somewhere
                content_extraction['inferlink_posts'] = ifl_extractions
                field_name_special_text = 'inferlink_posts_special_text'
                content_extraction[field_name_special_text] = dict()
                content_extraction[field_name_special_text][_TEXT] = self.inferlink_posts_to_text(ifl_extractions)
                ifl_extractions = ifl_extractions[0]

            if ifl_extractions and len(ifl_extractions.keys()) > 0:
                description = ''
                content_extraction[field_name] = dict()
                for key in ifl_extractions:
                    if isinstance(ifl_extractions[key], basestring) or isinstance(ifl_extractions[key], numbers.Number):
                        if ifl_extractions[key]:
                            o = dict()
                            if key == 'post_content' or 'content' in key or 'description' in key:
                                new_key = _INFERLINK_DESCRIPTION
                                description += ifl_extractions[key] + '\n'
                            else:
                                new_key = key

                            o[new_key] = dict()
                            if 'date' in key:
                                o[new_key]['text'] = ifl_extractions[key][:30] if len(ifl_extractions[key]) > 30 else \
                                    ifl_extractions[key]
                            else:
                                o[new_key]['text'] = ifl_extractions[key]
                            content_extraction[field_name].update(o)
                if description:
                    content_extraction[field_name][_INFERLINK_DESCRIPTION][_TEXT] = description
        return content_extraction

    @staticmethod
    def inferlink_posts_to_text(inferlink_posts):
        text = ''
        for inferlink_post in inferlink_posts:
            for k, v in inferlink_post.iteritems():
                if k == 'review_details':
                    for pair in v:
                        if 'key' in pair and 'value' in pair:
                            text += '{}_{}: {}\n'.format('review_details', pair['key'], pair['value'])
                else:
                    text += '{}: {}\n'.format(k, v)
        return text

    def consolidate_landmark_rules(self):
        rules = dict()
        if _RESOURCES in self.extraction_config:
            resources = self.extraction_config[_RESOURCES]
            if _LANDMARK in resources:
                landmark_rules_file_list = resources[_LANDMARK]
                for landmark_rules_file in landmark_rules_file_list:
                    rules.update(Core.load_json_file(landmark_rules_file))
                return rules
            else:
                raise KeyError('{}.{} not found in provided extraction config'.format(_RESOURCES, _LANDMARK))
        else:
            raise KeyError('{} not found in provided extraction config'.format(_RESOURCES))

    def get_dict_file_name_from_config(self, dict_name):
        if _RESOURCES in self.extraction_config:
            resources = self.extraction_config[_RESOURCES]
            if _DICTIONARIES in resources:
                if dict_name in resources[_DICTIONARIES]:
                    return resources[_DICTIONARIES][dict_name]
                else:
                    raise KeyError(
                        '{}.{}.{} not found in provided extraction config'.format(_RESOURCES, _DICTIONARIES, dict_name))
            else:
                raise KeyError('{}.{} not found in provided extraction config'.format(_RESOURCES, _DICTIONARIES))
        else:
            raise KeyError('{} not found in provided extraction config'.format(_RESOURCES))

    def get_stop_word_dictionary_name_from_config(self, dict_name):
        if _RESOURCES in self.extraction_config:
            if _STOP_WORD_DICTIONARIES in self.extraction_config[_RESOURCES]:
                if dict_name in self.extraction_config[_RESOURCES][_STOP_WORD_DICTIONARIES]:
                    return self.extraction_config[_RESOURCES][_STOP_WORD_DICTIONARIES][dict_name]
        return None

    def get_pickle_file_name_from_config(self, pickle_name):
        if _RESOURCES in self.extraction_config:
            resources = self.extraction_config[_RESOURCES]
            if _PICKLES in resources:
                if pickle_name in resources[_PICKLES]:
                    return resources[_PICKLES][pickle_name]
                else:
                    raise KeyError(
                        '{}.{}.{} not found in provided extraction config'.format(_RESOURCES, _PICKLES, pickle_name))
            else:
                raise KeyError('{}.{} not found in provided extraction config'.format(_RESOURCES, _PICKLES))
        else:
            raise KeyError('{} not found in provided extraction config'.format(_RESOURCES))

    def get_spacy_field_rules_from_config(self, field_name):
        if _RESOURCES in self.extraction_config:
            resources = self.extraction_config[_RESOURCES]
            if _SPACY_FIELD_RULES in resources:
                if field_name in resources[_SPACY_FIELD_RULES]:
                    return resources[_SPACY_FIELD_RULES][field_name]
                else:
                    raise KeyError(
                        '{}.{}.{} not found in provided extraction config'.format(_RESOURCES, _SPACY_FIELD_RULES,
                                                                                  field_name))
            else:
                raise KeyError('{}.{} not found in provided extraction config'.format(_RESOURCES, _SPACY_FIELD_RULES))
        else:
            raise KeyError('{} not found in provided extraction config'.format(_RESOURCES))

    def run_title(self, content_extraction, html, title_config):
        field_name = title_config[_FIELD_NAME] if _FIELD_NAME in title_config else _TITLE
        ep = self.determine_extraction_policy(title_config)
        if field_name not in content_extraction or (field_name in content_extraction and ep == _REPLACE):
            extracted_title = self.extract_title(html)
            if extracted_title:
                content_extraction[field_name] = extracted_title
        return content_extraction

    def run_table_extractor(self, content_extraction, html, table_config):
        field_name = table_config[_FIELD_NAME] if _FIELD_NAME in table_config else _TABLE
        ep = self.determine_extraction_policy(table_config)
        if field_name not in content_extraction or (field_name in content_extraction and ep == _REPLACE):
            tables = self.extract_table(html, table_config)
            if tables is not None:
                content_extraction[field_name] = tables
        return content_extraction

    def assert_data_extraction_guard(self, guards, doc, json_path_result):
        # print 'processing guards: {}'.format(guards)
        for guard in guards:
            try:
                if guard['path'] not in self.guards_path_regex:
                    self.guards_path_regex[guard['path']] = parse(guard['path'])
                jpath_parser = self.guards_path_regex[guard['path']]
                regex = guard['regex']
                if guard['type'] == 'doc':
                    matches = jpath_parser.find(doc)
                elif guard['type'] == 'path':
                    matches = jpath_parser.find(json_path_result)
                else:
                    print
                    'guard type "{}" is not a valid type.'.format(guard['type'])
                    continue
                # if len(matches) == 0:
                #     return False
                for match in matches:
                    # print match.value, regex
                    if not re.match(regex, match.value):
                        return False
            except Exception as e:
                print
                'could not apply guard: {}'.format(guard)
        return True

    def run_readability(self, content_extraction, html, re_extractor):
        recall_priority = False
        field_name = None
        readability_text = None
        if _STRICT in re_extractor:
            recall_priority = False if re_extractor[_STRICT] == _YES else True
            field_name = _CONTENT_RELAXED if recall_priority else _CONTENT_STRICT
        options = {_RECALL_PRIORITY: recall_priority}

        if _FIELD_NAME in re_extractor:
            field_name = re_extractor[_FIELD_NAME]
        ep = self.determine_extraction_policy(re_extractor)
        timeout = re_extractor[_TIMEOUT] if _TIMEOUT in re_extractor else self.readability_timeout
        signal.signal(signal.SIGALRM, self.timeout_handler)
        signal.alarm(timeout)
        try:
            readability_text = self.extract_readability(html, options)
            signal.alarm(0)
        except TimeoutException:
            pass

        if readability_text:
            if field_name not in content_extraction or (field_name in content_extraction and ep == _REPLACE):
                content_extraction[field_name] = readability_text
        return content_extraction

    def determine_extraction_policy(self, config):
        ep = _REPLACE
        if not config:
            return ep
        if _EXTRACTION_POLICY in config:
            ep = config[_EXTRACTION_POLICY]
        elif self.global_extraction_policy:
            ep = self.global_extraction_policy
        if ep and ep != _KEEP_EXISTING and ep != _REPLACE:
            raise ValueError('extraction_policy can either be {} or {}'.format(_KEEP_EXISTING, _REPLACE))
        return ep

    @staticmethod
    def _relevant_text_from_context(text_or_tokens, results, field_name):
        if results:
            tokens_len = len(text_or_tokens)
            if not isinstance(results, list):
                results = [results]
            for result in results:
                if 'context' in result:
                    start = int(result['context']['start'])
                    end = int(result['context']['end'])
                    if isinstance(text_or_tokens, basestring):
                        if start - 10 < 0:
                            new_start = 0
                        else:
                            new_start = start - 10
                        if end + 10 > tokens_len:
                            new_end = tokens_len
                        else:
                            new_end = end + 10
                        relevant_text = '<etk \'attribute\' = \'{}\'>{}</etk>'.format(field_name,
                                                                                      text_or_tokens[start:end].encode(
                                                                                          'utf-8'))
                        result['context']['text'] = '{} {} {}'.format(text_or_tokens[new_start:start].encode('utf-8'),
                                                                      relevant_text,
                                                                      text_or_tokens[end:new_end].encode('utf-8'))
                        result['context']['input'] = _TEXT
                    else:
                        if start - 5 < 0:
                            new_start = 0
                        else:
                            new_start = start - 5
                        if end + 5 > tokens_len:
                            new_end = tokens_len
                        else:
                            new_end = end + 5
                        relevant_text = '<etk \'attribute\' = \'{}\'>{}</etk>'.format(field_name,
                                                                                      ' '.join(text_or_tokens[
                                                                                               start:end]).encode(
                                                                                          'utf-8'))
                        result['context']['text'] = '{} {} {} '.format(
                            ' '.join(text_or_tokens[new_start:start]).encode('utf-8'),
                            relevant_text,
                            ' '.join(text_or_tokens[end:new_end]).encode('utf-8'))
                        # result['context']['tokens_left'] = text_or_tokens[new_start:start]
                        # result['context']['tokens_right'] = text_or_tokens[end:new_end]
                        result['context']['input'] = _TOKENS
        return results

    @staticmethod
    def sort_dict(dictionary):
        return collections.OrderedDict(sorted(dictionary.items()))

    @staticmethod
    def load_json_file(file_name):
        json_x = json.load(codecs.open(file_name, 'r'))
        return json_x

    @staticmethod
    def process_decoding_dict(decoding_dict):
        # lower the keys so that we can do a string match properly
        new_dict = dict()
        for k in decoding_dict.keys():
            try:
                new_dict[k.lower()] = decoding_dict[k]
            except:
                # some weird unicode probably
                new_dict[k] = decoding_dict[k]
        return new_dict

    def load_json(self, json_name):
        if json_name not in self.jobjs:
            self.jobjs[json_name] = self.load_json_file(self.get_pickle_file_name_from_config(json_name))
        return self.jobjs[json_name]

    def load_trie(self, file_name, case_sensitive=False):
        try:
            values = json.load(gzip.open(file_name), 'utf-8')
        except:
            values = None
        if not values:
            values = json.load(codecs.open(file_name), 'utf-8')

        if case_sensitive:
            trie = dictionary_extractor.populate_trie(map(lambda x: x, values))
        else:
            trie = dictionary_extractor.populate_trie(map(lambda x: x.lower(), values))
        return trie

    def load_dictionary(self, field_name, dict_name, case_sensitive):
        if field_name not in self.tries:
            self.tries[field_name] = self.load_trie(self.get_dict_file_name_from_config(dict_name), case_sensitive)

    def load_stop_words(self, field_name, dict_name):
        if field_name not in self.stop_word_dicts:
            dict_path = self.get_stop_word_dictionary_name_from_config(dict_name)
            if os.path.exists(dict_path):
                try:
                    self.stop_word_dicts[field_name] = json.load(gzip.open(dict_path), 'utf-8')
                except:
                    self.stop_word_dicts[field_name] = json.load(codecs.open(dict_path, 'r'))

    def load_pickle_file(self, pickle_path):
        return pickle.load(open(pickle_path, 'rb'))

    def load_pickle(self, pickle_name):
        if pickle_name not in self.pickles:
            self.pickles[pickle_name] = self.load_pickle_file(self.get_pickle_file_name_from_config(pickle_name))
        return self.pickles[pickle_name]

    def extract_using_dictionary(self, d, config):
        field_name = config[_FIELD_NAME]

        # case sensitivity is disabled by default
        case_sensitive = str(config[_CASE_SENSITIVE]).lower() == 'true' if _CASE_SENSITIVE in config else False

        # this method is self aware that it needs tokens as input
        if case_sensitive:
            tokens = d[_SIMPLE_TOKENS_ORIGINAL_CASE]
        else:
            tokens = d[_SIMPLE_TOKENS]

        if not tokens:
            return None
        if _DICTIONARY not in config:
            raise KeyError('No dictionary specified for {}'.format(field_name))

        self.load_dictionary(field_name, config[_DICTIONARY], case_sensitive)

        pre_process = None
        if _PRE_PROCESS in config and len(config[_PRE_PROCESS]) > 0:
            pre_process = self.string_to_lambda(config[_PRE_PROCESS][0])
        if not pre_process:
            pre_process = lambda x: x

        pre_filter = None
        if _PRE_FILTER in config and len(config[_PRE_FILTER]) > 0:
            pre_filter = self.string_to_lambda(config[_PRE_FILTER][0])
        if not pre_filter:
            pre_filter = lambda x: x

        post_filter = None
        if _PRE_FILTER in config and len(config[_PRE_FILTER]) > 0:
            post_filter = self.string_to_lambda(config[_PRE_FILTER][0])
        if not post_filter:
            post_filter = lambda x: isinstance(x, basestring)

        ngrams = int(config[_NGRAMS]) if _NGRAMS in config else 1

        joiner = config[_JOINER] if _JOINER in config else ' '

        results = self._extract_using_dictionary(tokens, pre_process,
                                                 self.tries[
                                                     field_name],
                                                 pre_filter,
                                                 post_filter,
                                                 ngrams, joiner)
        if _POST_FILTER_S in config:
            post_filters = config[_POST_FILTER_S]
            results = self.run_post_filters_results(results, post_filters, field_name=field_name)

        return self._relevant_text_from_context(tokens, results, field_name)

    @staticmethod
    def _extract_using_dictionary(tokens, pre_process, trie, pre_filter, post_filter, ngrams, joiner):
        result = dictionary_extractor.extract_using_dictionary(tokens, pre_process=pre_process,
                                                               trie=trie,
                                                               pre_filter=pre_filter,
                                                               post_filter=post_filter,
                                                               ngrams=ngrams,
                                                               joiner=joiner)
        return result if result and len(result) > 0 else None

    def extract_website_domain(self, d, config):
        text = d[_TEXT]
        field_name = config[_FIELD_NAME]
        tld = config[_TLD] if _TLD in config else self.extract_tld(text)
        results = {"value": tld}
        return self._relevant_text_from_context(d[_TEXT], results, field_name)

    def extract_using_regex(self, d, config):
        # this method is self aware that it needs the text, so look for text in the input d
        text = d[_TEXT]
        include_context = True
        if "include_context" in config and config['include_context'].lower() == 'false':
            include_context = False
        if "regex" not in config:
            raise KeyError('No regular expression found in {}'.format(json.dumps(config)))
        regex = config["regex"]
        flags = 0
        if "regex_options" in config:
            regex_options = config['regex_options']
            if not isinstance(regex_options, list):
                raise ValueError("regular expression options should be a list in {}".format(json.dumps(config)))
            for regex_option in regex_options:
                flags = flags | eval("re." + regex_option)
        if _PRE_FILTER in config:
            text = self.run_user_filters(d, config[_PRE_FILTER], config[_FIELD_NAME])

        result = self._extract_using_regex(text, regex, include_context, flags)
        # TODO ADD code to handle post_filters
        return self._relevant_text_from_context(d[_TEXT], result, config[_FIELD_NAME])

    @staticmethod
    def _extract_using_regex(text, regex, include_context, flags):
        try:
            result = regex_extractor.extract(text, regex, include_context, flags)
            return result if result and len(result) > 0 else None
        except Exception as e:
            print
            e
            return None

    def extract_using_custom_spacy(self, d, config, field_rules=None):
        if not field_rules:
            field_rules = self.load_json_file(self.get_spacy_field_rules_from_config(config[_SPACY_FIELD_RULES]))
        if not self.nlp:
            self.prep_spacy()

        # call the custom spacy extractor
        # nlp_doc = self.nlp(d[_SIMPLE_TOKENS_ORIGINAL_CASE], parse=False)
        nlp_doc = self.nlp(d[_SIMPLE_TOKENS_ORIGINAL_CASE])
        results = self._relevant_text_from_context(d[_SIMPLE_TOKENS_ORIGINAL_CASE],
                                                   custom_spacy_extractor.extract(field_rules, nlp_doc, self.nlp),
                                                   config[_FIELD_NAME])

        if _POST_FILTER in config:
            post_filters = config[_POST_FILTER]
            results = self.run_post_filters_results(results, post_filters, field_name=config[_FIELD_NAME])

        return results

    def infer_rule_using_custom_spacy(self, d, positive_eg):
        t = TokenizerExtractor(recognize_linebreaks=True, create_structured_tokens=True)
        if not self.nlp:
            self.prep_spacy()

        # call the custom spacy inferer
        nlp_doc = self.nlp(d[_SIMPLE_TOKENS_ORIGINAL_CASE], parse=False)
        results = custom_spacy_extractor.infer_rule(nlp_doc, self.nlp, positive_eg, t)
        return results

    def extract_using_spacy(self, d, config):
        field_name = config[_FIELD_NAME]
        if not self.nlp:
            self.prep_spacy()
        if not self.origin_nlp:
            self.prep_origin_spacy()

        nlp_doc = self.nlp(d[_SIMPLE_TOKENS], parse=False)
        self.load_matchers(field_name)
        results = None
        if field_name == _AGE:
            results = self._relevant_text_from_context(d[_SIMPLE_TOKENS],
                                                       spacy_age_extractor.extract(nlp_doc, self.matchers[_AGE]), _AGE)
        elif field_name == _POSTING_DATE or _DATE in field_name:
            self.load_matchers(_POSTING_DATE)
            results = self._relevant_text_from_context(d[_SIMPLE_TOKENS],
                                                       spacy_date_extractor.extract(nlp_doc,
                                                                                    self.matchers[_POSTING_DATE]),
                                                       field_name)
            if _POST_FILTER in config:
                post_filters = config[_POST_FILTER]
                results = self.run_post_filters_results(results, post_filters, field_name=field_name)

        elif field_name == _SOCIAL_MEDIA:
            results = self._relevant_text_from_context(d[_SIMPLE_TOKENS],
                                                       spacy_social_media_extractor.extract(nlp_doc,
                                                                                            self.matchers[
                                                                                                _SOCIAL_MEDIA]),
                                                       _SOCIAL_MEDIA)
        elif field_name == _ADDRESS:
            results = self._relevant_text_from_context(d[_SIMPLE_TOKENS],
                                                       spacy_address_extractor.extract(nlp_doc,
                                                                                       self.matchers[_ADDRESS]),
                                                       _ADDRESS)

        elif field_name == _EMAIL:
            t = TokenizerExtractor(recognize_linebreaks=True, create_structured_tokens=True)
            # print spacy_email_extractor.extract(d[_TEXT], self.origin_nlp, self.nlp, t)
            results = self._relevant_text_from_context(d[_SIMPLE_TOKENS],
                                                       spacy_email_extractor.extract(d[_TEXT], self.origin_nlp,
                                                                                     self.nlp, t),
                                                       _EMAIL)
        return results

    def extract_using_default_spacy(self, d, config):
        if not self.nlp:
            self.prep_spacy()

        spacy_to_etk_mapping = config.get('spacy_to_etk_mapping', None)
        if spacy_to_etk_mapping is None:
            results = list()
        else:
            nlp_doc = self.nlp(d[_SIMPLE_TOKENS_ORIGINAL_CASE])
            results = default_spacy_extractor.extract(nlp_doc, spacy_to_etk_mapping)

        modified_results = dict()
        for field_name, result in results.items():
            modified_results[field_name] = self._relevant_text_from_context(d[_SIMPLE_TOKENS_ORIGINAL_CASE], result,
                                                                            field_name)

        return modified_results

    def extract_from_landmark(self, doc, config, selected_field=None):
        field_name = config[_FIELD_NAME]
        if _CONTENT_EXTRACTION not in doc:
            return None
        if _INFERLINK_EXTRACTIONS not in doc[_CONTENT_EXTRACTION]:
            return None
        results = list()
        inferlink_extraction = doc[_CONTENT_EXTRACTION][_INFERLINK_EXTRACTIONS]
        pre_filters = None
        if _PRE_FILTER in config:
            pre_filters = config[_PRE_FILTER]

        post_filters = None
        if _POST_FILTER in config:
            post_filters = config[_POST_FILTER]
        if selected_field:
            if selected_field in inferlink_extraction:
                d = inferlink_extraction[selected_field]
                if pre_filters:
                    # Assumption all pre_filters are lambdas
                    d[_TEXT] = self.run_user_filters(d, pre_filters, config[_FIELD_NAME])
                result = None
                if post_filters:
                    post_result = self.run_user_filters(d, post_filters, config[_FIELD_NAME])
                    if post_result:
                        result = self.handle_text_or_results(post_result)
                else:
                    result = self.handle_text_or_results(d[_TEXT])
                if result:
                    results.extend(result)
        else:
            for field in inferlink_extraction.keys():
                # The logic below: if the inferlink rules do not have semantic information in the field names returned,
                #                                                                                               too bad
                if field_name in field:
                    d = inferlink_extraction[field]
                    if pre_filters:
                        # Assumption all pre_filters are lambdas
                        d[_TEXT] = self.run_user_filters(d, pre_filters, config[_FIELD_NAME])

                    result = None
                    if post_filters:
                        post_result = self.run_user_filters(d, post_filters, config[_FIELD_NAME])
                        if post_result:
                            result = self.handle_text_or_results(post_result)
                    else:
                        result = self.handle_text_or_results(d[_TEXT])
                    if result:
                        results.extend(result)
        return results if len(results) > 0 else None

    def extract_phone(self, d, config):
        tokens = d[_SIMPLE_TOKENS]
        # source type as in text vs url #SHRUG
        source_type = config[_SOURCE_TYPE] if _SOURCE_TYPE in config else 'text'
        include_context = True
        output_format = _OBFUSCATION
        # if _PRE_FILTER in config:
        #     text = self.run_user_filters(d, config[_PRE_FILTER], config[_FIELD_NAME])
        return self._relevant_text_from_context(d[_SIMPLE_TOKENS],
                                                self._extract_phone(tokens, source_type, include_context,
                                                                    output_format), config[_FIELD_NAME])

    @staticmethod
    def _extract_phone(tokens, source_type, include_context, output_format):
        result = phone_extractor.extract(tokens, source_type, include_context, output_format)
        if isinstance(result, dict):
            result = [result]
        new_result = list()
        for r in result:
            val = r['value']
            if len(val) <= 10 or val.startswith('+') or val.startswith('1'):
                new_result.append(r)
        return new_result if len(new_result) > 0 else None

    def extract_email(self, d, config):
        text = d[_TEXT]
        include_context = True
        if _INCLUDE_CONTEXT in config:
            include_context = config[_INCLUDE_CONTEXT].upper() == 'TRUE'
        if _PRE_FILTER in config:
            text = self.run_user_filters(d, config[_PRE_FILTER], config[_FIELD_NAME])
        return self._relevant_text_from_context(d[_TEXT], self._extract_email(text, include_context),
                                                config[_FIELD_NAME])

    @staticmethod
    def _extract_email(text, include_context):
        """
        A regular expression based function to extract emails from text
        :param text: The input text.
        :param include_context: True or False, will include context matched by the regular expressions.
        :return: An object, with extracted email and/or context.
        """
        return email_extractor.extract(text, include_context)

    def extract_price(self, d, config):
        text = d[_TEXT]
        if _PRE_FILTER in config:
            text = self.run_user_filters(d, config[_PRE_FILTER], config[_FIELD_NAME])
        return self._relevant_text_from_context(d[_TEXT], self._extract_price(text), config[_FIELD_NAME])

    @staticmethod
    def _extract_price(text):
        return price_extractor.extract(text)

    def extract_height(self, d, config):
        text = d[_TEXT]
        if _PRE_FILTER in config:
            text = self.run_user_filters(d, config[_PRE_FILTER], config[_FIELD_NAME])
        return self._relevant_text_from_context(d[_TEXT], self._extract_height(text), config[_FIELD_NAME])

    @staticmethod
    def _extract_height(text):
        return height_extractor.extract(text)

    def extract_weight(self, d, config):
        text = d[_TEXT]
        if _PRE_FILTER in config:
            text = self.run_user_filters(d, config[_PRE_FILTER], config[_FIELD_NAME])
        return self._relevant_text_from_context(d[_TEXT], self._extract_weight(text), config[_FIELD_NAME])

    @staticmethod
    def _extract_weight(text):
        return weight_extractor.extract(text)

    def extract_address(self, d, config):
        text = d[_TEXT]
        if _PRE_FILTER in config:
            text = self.run_user_filters(d, config[_PRE_FILTER], config[_FIELD_NAME])
        return self._relevant_text_from_context(d[_TEXT], self._extract_address(text), config[_FIELD_NAME])

    @staticmethod
    def _extract_address(text):
        return address_extractor.extract(text)

    def extract_age(self, d, config):
        text = d[_TEXT]
        if _PRE_FILTER in config:
            text = self.run_user_filters(d, config[_PRE_FILTER], config[_FIELD_NAME])
        results = self._extract_age(text)
        if _POST_FILTER in config:
            post_filters = config[_POST_FILTER]
            results = self.run_post_filters_results(results, post_filters, field_name=config[_FIELD_NAME])
        return self._relevant_text_from_context(d[_TEXT], results, config[_FIELD_NAME])

    @staticmethod
    def _extract_age(text):
        return age_extractor.extract(text)

    def extract_review_id(self, d, config):
        text = d[_TEXT]
        if _PRE_FILTER in config:
            text = self.run_user_filters(d, config[_PRE_FILTER], config[_FIELD_NAME])
        return self._relevant_text_from_context(d[_TEXT], self._extract_review_id(text), config[_FIELD_NAME])

    @staticmethod
    def _extract_review_id(text):
        return review_id_extractor.extract(text)

    @staticmethod
    def handle_text_or_results(x):
        if isinstance(x, basestring) or isinstance(x, numbers.Number):
            o = dict()
            if isinstance(x, numbers.Number):
                x = str(x)
            o['value'] = x
            return [o]
        if isinstance(x, dict):
            return [x]
        if isinstance(x, list):
            return x
        return None

    def run_user_filters(self, d, filters, field_name):
        result = None
        if not isinstance(filters, list):
            filters = [filters]
        try:
            for text_filter in filters:
                try:
                    f = getattr(self, text_filter)
                    if f:
                        result = f(d, {_FIELD_NAME: field_name})
                except Exception as e:
                    result = None
                if not result:
                    result = Core.string_to_lambda(text_filter)(d[_TEXT])
        except Exception as e:
            print
            'Error {} in {}'.format(e, 'run_user_filters')
        return result

    def run_post_filters_results(self, results, post_filters, field_name=None):
        if results:
            if not isinstance(results, list):
                results = [results]
            if not isinstance(post_filters, list):
                post_filters = [post_filters]
            out_results = list()
            for post_filter in post_filters:
                try:
                    f = getattr(self, post_filter)
                    if f:
                        for result in results:
                            val = f(result['value'], field_name=field_name)
                            if val:
                                result['value'] = val
                                out_results.append(result)
                except:
                    print
                    'Warn: No function {} defined in core.py'.format(post_filter)
                    # lets try lambda functions
                    for result in results:
                        val = Core.string_to_lambda(post_filter)(result['value'])
                        if val:
                            result['value'] = val
                            out_results.append(result)
            return out_results if len(out_results) > 0 else None

    @staticmethod
    def string_to_lambda(s):
        try:
            return lambda x: eval(s)
        except:
            print
            'Error while converting {} to lambda'.format(s)
            return None

    @staticmethod
    def extract_readability(document, options=None):
        e = ReadabilityExtractor()
        return e.extract(document, options)

    def extract_title(self, html_content, options=None):
        if html_content:
            matches = re.search(self.html_title_regex, html_content, re.IGNORECASE | re.S)
            title = None
            if matches:
                title = matches.group(1)
                title = title.replace('\r', '')
                title = title.replace('\n', '')
                title = title.replace('\t', '')
            if not title:
                title = ''
            return {'text': title}
        return None

    @staticmethod
    def extract_crftokens(text, options=None, lowercase=True, create_structured_tokens=True):
        t = TokenizerExtractor(recognize_linebreaks=True, create_structured_tokens=create_structured_tokens)
        return t.extract(text, lowercase)

    @staticmethod
    def crftokens_to_lower(crf_tokens):
        lower_crf = copy.deepcopy(crf_tokens)
        for tk in lower_crf:
            tk['value'] = tk['value'].lower()
        return lower_crf

    @staticmethod
    def extract_tokens_from_crf(crf_tokens):
        return [tk['value'] for tk in crf_tokens]

    @staticmethod
    def extract_tokens_faithful(text, options=None):
        ft = FaithfulTokenizerExtractor(recognize_linebreaks=True, create_structured_tokens=True)
        return ft.extract(text)

    @staticmethod
    def extract_tokens_from_faithful(faithful_tokens):
        return [tk['value'] for tk in faithful_tokens]

    @staticmethod
    def filter_tokens(original_tokens, config):
        # config contains a list of types of tokens to be removed
        # [alphabet, digit, emoji, punctuation, html, html_entity, break]
        ft = FaithfulTokenizerExtractor(recognize_linebreaks=True, create_structured_tokens=True)
        ft.faithful_tokens = original_tokens
        # Return Tokens object which contains - tokens, reverse_map attributes
        # The object also has a method get_original_index() to retrieve index in faithful tokens
        return ft.filter_tokens(config)

    def extract_table(self, d, config):
        if _CONFIG in config:
            config = config[_CONFIG]
        te = table_extractor.TableExtraction()
        return te.extract(d)

    def entity_table_extractor(self, d, config):
        dic = set()
        # print config
        if 'dic' in config:
            # config = config[_CONFIG]
            dic = config['dic']
            dic = self.load_json(dic)

        te = table_extractor.EntityTableDataExtraction()
        res = te.extract(d, dic)
        return res if len(res) > 0 else None

    @staticmethod
    def extract_landmark(html, url, extraction_rules, threshold=0.5):
        return landmark_extraction.extract(html, url, extraction_rules, threshold)

    def prep_spacy(self):
        # self.nlp = spacy.load('en', entity=True)
        self.nlp = spacy.load('en')
        self.old_tokenizer = self.nlp.tokenizer
        self.nlp.tokenizer = lambda tokens: self.old_tokenizer.tokens_from_list(tokens)

    def prep_origin_spacy(self):
        self.origin_nlp = spacy.load('en')

    def load_matchers(self, field_name=None):
        if field_name:
            if field_name == _AGE:
                if _AGE not in self.matchers:
                    self.matchers[_AGE] = spacy_age_extractor.load_age_matcher(self.nlp)
            if field_name == _POSTING_DATE:
                if _POSTING_DATE not in self.matchers:
                    self.matchers[_POSTING_DATE] = spacy_date_extractor.load_date_matcher(self.nlp)
            if field_name == _SOCIAL_MEDIA:
                if _SOCIAL_MEDIA not in self.matchers:
                    self.matchers[_SOCIAL_MEDIA] = spacy_social_media_extractor.load_social_media_matcher(self.nlp)
            if field_name == _ADDRESS:
                if _ADDRESS not in self.matchers:
                    self.matchers[_ADDRESS] = spacy_address_extractor.load_address_matcher(self.nlp)

    @staticmethod
    def create_list_data_extraction(data_extraction, field_name, method=_EXTRACT_USING_DICTIONARY):
        out = list()
        if data_extraction:
            if field_name in data_extraction:
                extractions = data_extraction[field_name]
                if method in extractions:
                    out = Core.get_value_list_from_results(extractions[method]['results'])
        return out

    @staticmethod
    def get_value_list_from_results(results):
        out = list()
        if results:
            for result in results:
                out.append(result['value'])
        return out

    def extract_country_url(self, d, config):
        if not self.country_code_dict:
            try:
                self.country_code_dict = self.load_json_file(self.get_dict_file_name_from_config('country_code'))
            except:
                raise Exception('{} dictionary missing from resources'.format('country_code'))

        tokens_url = d[_SIMPLE_TOKENS]
        return self._relevant_text_from_context(tokens_url,
                                                url_country_extractor.extract(tokens_url, self.country_code_dict),
                                                config[_FIELD_NAME])

    def geonames_lookup(self, d, config):
        if not self.geonames_dict:
            try:
                self.geonames_dict = self.load_json_file(self.get_dict_file_name_from_config(_GEONAMES))
            except Exception:
                raise Exception('{} dictionary missing from resources'.format(_GEONAMES))

        if _CITY_NAME in d[_KNOWLEDGE_GRAPH]:
            cities = [x['key'] for x in d[_KNOWLEDGE_GRAPH][_CITY_NAME]]
        else:
            return None
        populated_places = self.add_origin_info(geonames_extractor.get_populated_places(cities, self.geonames_dict),
                                                'geonames_lookup', 'post_process', 1.0, d[_DOCUMENT_ID])
        return populated_places

    def decode_value(self, d, field_name=None):
        if field_name and field_name in self.decoding_dict_dict:
            decoding_dict = self.decoding_dict_dict[field_name]
            d = d.strip().lower()
            if d in decoding_dict and decoding_dict[d]:
                return decoding_dict[d]
        return d

    @staticmethod
    def parse_date(d, config=None, field_name=None, strict_parsing=True):
        ignore_past_years = config['ignore_past_years'] if config and 'ignore_past_years' in config else 20
        ignore_future_dates = config['ignore_future_dates'] if config and 'ignore_future_dates' in config else True
        if isinstance(d, basestring):
            return Core.spacy_parse_date(d, ignore_past_years, ignore_future_dates, strict_parsing=strict_parsing)
        else:
            try:
                return date_parser.convert_to_iso_format(
                    date_parser.parse_date(d[_TEXT], ignore_future_dates=ignore_future_dates,
                                           ignore_past_years=ignore_past_years, strict_parsing=strict_parsing))
            except:
                return None

    @staticmethod
    def parse_date_generic(d, config=None, field_name=None):
        if not config:
            config = dict()
        config['ignore_past_years'] = 200
        config['ignore_future_dates'] = False

        try:
            # try the 2005344 format just in case

            to_be_parsed_date = str(d) if isinstance(d, basestring) else d[_TEXT]
            if seven_digits.match(to_be_parsed_date):
                year = to_be_parsed_date[0:4]
                day_of_year = to_be_parsed_date[4:7]
                parsed_date = datetime.datetime.strptime('{} {}'.format(year, day_of_year), '%Y %j')
                return parsed_date.isoformat()
        except:
            return None
        result = Core.parse_date(d, config=config, strict_parsing=False)

        return result

    @staticmethod
    def spacy_parse_date(str_date, ignore_past_years=20, ignore_future_dates=True, strict_parsing=True):
        try:
            return date_parser.convert_to_iso_format(
                date_parser.parse_date(str_date, ignore_future_dates=ignore_future_dates,
                                       ignore_past_years=ignore_past_years, strict_parsing=strict_parsing))
        except:
            return None

    @staticmethod
    def filter_age(d, config=None, field_name=None):
        if isinstance(d, basestring) or isinstance(d, numbers.Number):
            text = d
        else:
            text = d[_TEXT]
        try:
            text = text.replace('\n', '')
            text = text.replace('\t', '')
            num = int(text)
            return num if 18 <= num <= 65 else None
        except:
            pass
        return None

    @staticmethod
    def parse_number(d, config=None, field_name=None):
        if isinstance(d, basestring) or isinstance(d, numbers.Number):
            text = d
        elif isinstance(d, dict) and _TEXT in d:
            text = d[_TEXT]
        else:
            return None

        if isinstance(text, numbers.Number):
            return str(text)

        try:
            text = text.strip().replace('\n', '').replace('\t', '').replace(',', '')
            num = str(float(text)) if '.' in text else str(int(text))
            return num
        except:
            pass
        return None

    def country_from_states(self, d, config):
        if not self.state_to_country_dict:
            try:
                self.state_to_country_dict = self.load_json_file(self.get_dict_file_name_from_config(_STATE_TO_COUNTRY))
            except Exception:
                raise Exception('{} dictionary missing from resources'.format(_STATE_TO_COUNTRY))

        if _STATE in d[_KNOWLEDGE_GRAPH]:
            states = [x['key'] for x in d[_KNOWLEDGE_GRAPH][_STATE]]
        else:
            return None

        return geonames_extractor.get_country_from_states(states, self.state_to_country_dict)

    def country_feature(self, d, config):
        return country_classifier.calc_country_feature(d[_KNOWLEDGE_GRAPH], self.state_to_country_dict)

    def create_city_state_country_triple(self, d, config):
        if not self.state_to_codes_lower_dict:
            try:
                self.state_to_codes_lower_dict = self.load_json_file(
                    self.get_dict_file_name_from_config(_STATE_TO_CODES_LOWER))
            except Exception as e:
                raise ValueError('{} dictionary missing from resources'.format(_STATE_TO_CODES_LOWER))
        if not self.populated_cities:
            try:
                self.populated_cities = self.load_json_file(self.get_dict_file_name_from_config(_POPULATED_CITIES))
            except Exception as e:
                raise ValueError('{} dictionary missing from resources'.format(_POPULATED_CITIES))

        try:
            priori_lst = ['city_state_together', 'city_state_code_together',
                          'city_country_together', 'city_state_separate',
                          'city_country_separate', 'city_state_code_separate']
            results = [[] for i in range(len(priori_lst) + 1)]
            knowledge_graph = d[_KNOWLEDGE_GRAPH]
            if "populated_places" in knowledge_graph:
                pop_places = knowledge_graph["populated_places"]
                for place in pop_places:
                    city_state_together_count = 0
                    city_state_separate_count = 0
                    city_state_code_together_count = 0
                    city_state_code_separate_count = 0
                    city_country_together_count = 0
                    city_country_separate_count = 0
                    city = place["value"]

                    state = place['provenance'][0]['qualifiers'][_STATE] if _STATE in place['provenance'][0][
                        'qualifiers'] else ""

                    # in some cases, place['provenance'][0]['qualifiers'][_STATE] might be None
                    if not state:
                        state = ''

                    country = place['provenance'][0]['qualifiers'][_COUNTRY] if _COUNTRY in place['provenance'][0][
                        'qualifiers'] else ""

                    # in some cases, place['provenance'][0]['qualifiers'][_COUNTRY] might be None
                    if not country:
                        country = ''
                    document_id = place['provenance'][0]['source'][_DOCUMENT_ID]

                    if state in self.state_to_codes_lower_dict:
                        state_code = self.state_to_codes_lower_dict[state]
                    else:
                        state_code = None

                    cities = list()

                    if _CITY_NAME in knowledge_graph:
                        city_name_objects = knowledge_graph[_CITY_NAME]
                        for city_name_object in city_name_objects:
                            if city == city_name_object["value"]:
                                for prov in city_name_object["provenance"]:
                                    if "context" in prov["source"]:
                                        cities.append((prov["source"]["segment"], prov["source"]["context"]["start"],
                                                       prov["source"]["context"]["end"]))

                    states = list()
                    if country == "united states":
                        if _STATE in knowledge_graph:
                            state_objects = knowledge_graph[_STATE]
                            for state_object in state_objects:
                                if state == state_object["value"]:
                                    for prov in state_object["provenance"]:
                                        if "context" in prov["source"]:
                                            states.append(
                                                (prov["source"]["segment"], prov["source"]["context"]["start"],
                                                 prov["source"]["context"]["end"]))

                    countries = list()
                    if _COUNTRY in knowledge_graph:
                        country_objects = knowledge_graph[_COUNTRY]
                        for country_object in country_objects:
                            if country == country_object["value"]:
                                for prov in country_object["provenance"]:
                                    if "context" in prov["source"]:
                                        countries.append(
                                            (prov["source"]["segment"], prov["source"]["context"]["start"],
                                             prov["source"]["context"]["end"]))

                    state_codes = list()
                    if country == "united states":
                        if state_code:
                            if "states_usa_codes" in knowledge_graph:
                                states_usa_objects = knowledge_graph["states_usa_codes"]
                                for state_usa_object in states_usa_objects:
                                    if state_code == state_usa_object["value"]:
                                        for prov in state_usa_object["provenance"]:
                                            if "context" in prov["source"]:
                                                state_codes.append(
                                                    (prov["source"]["segment"], prov["source"]["context"]["start"],
                                                     prov["source"]["context"]["end"]))

                    if cities:
                        segments = list()
                        for a_city in cities:
                            for a_state in states:
                                if a_city[0] == a_state[0] and a_city[1] != a_state[1] and (
                                        abs(a_city[2] - a_state[1]) < 3 or abs(a_city[1] - a_state[2]) < 3):
                                    city_state_together_count += 1
                                    if a_city[0] not in segments:
                                        segments.append(a_city[0])
                                else:
                                    city_state_separate_count += 1
                            for a_state_code in state_codes:
                                if a_city[0] == a_state_code[0] and a_city[1] != a_state_code[1] and a_state_code[1] - \
                                        a_city[2] < 3 and a_state_code[1] - a_city[2] > 0:
                                    city_state_code_together_count += 1
                                    if a_city[0] not in segments:
                                        segments.append(a_city[0])
                                else:
                                    city_state_code_separate_count += 1
                            for a_country in countries:
                                if a_city[0] == a_country[0] and a_city[1] != a_country[1] and (
                                        abs(a_city[2] - a_country[1]) < 5 or abs(a_city[1] - a_country[2]) < 3):
                                    city_country_together_count += 1
                                    if a_city[0] not in segments:
                                        segments.append(a_city[0])
                                else:
                                    city_country_separate_count += 1

                        result = dict()
                        origin = dict()
                        origin['method'] = 'create_city_state_country_triple'
                        origin[_DOCUMENT_ID] = document_id
                        origin['score'] = 1.0

                        qualifiers = dict()
                        qualifiers['city_state_together'] = city_state_together_count
                        qualifiers['city_state_separate'] = city_state_separate_count
                        qualifiers['city_state_code_together'] = city_state_code_together_count
                        qualifiers['city_state_code_separate'] = city_state_code_separate_count
                        qualifiers['city_country_together'] = city_country_together_count
                        qualifiers['city_country_separate'] = city_country_separate_count
                        qualifiers['population'] = place["provenance"][0]["qualifiers"]['population']
                        qualifiers['longitude'] = place["provenance"][0]["qualifiers"]['longitude']
                        qualifiers['latitude'] = place["provenance"][0]["qualifiers"]['latitude']

                        result['metadata'] = qualifiers

                        for priori_idx, counter in enumerate(priori_lst):
                            if country == "united states":
                                result_value = city + ',' + state
                            else:
                                result_value = city + ',' + country
                            result['key'] = city + ':' + state + ':' + country + ':' + str(
                                place["provenance"][0]["qualifiers"]['longitude']) + ':' + str(
                                place["provenance"][0]["qualifiers"]['latitude'])
                            if qualifiers[counter] > 0:
                                if priori_idx < 3:
                                    result['value'] = result_value + "-1.0"
                                    origin['segment'] = counter + ' in'
                                    for segment in segments:
                                        origin['segment'] += ' ' + segment
                                elif priori_idx < 5:
                                    result['value'] = result_value + "-0.8"
                                    origin['segment'] = counter + ' in somewhere'
                                else:
                                    result['value'] = result_value + "-0.3"
                                    origin['segment'] = counter + ' in somewhere'
                                result['origin'] = origin
                                results[priori_idx].append(result)
                                break
                            else:
                                if isinstance(self.populated_cities, dict):
                                    if priori_idx == 5 and city in self.populated_cities:
                                        if self.populated_cities[city]["country"] == country:
                                            if "state" in self.populated_cities[city]:
                                                if self.populated_cities[city]["state"] == state:
                                                    result['value'] = result_value + "-0.1"
                                                    origin['segment'] = 'none'
                                                    result['origin'] = origin
                                                    results[priori_idx + 1].append(result)
                                            else:
                                                result['value'] = result_value + "-0.1"
                                                origin['segment'] = 'none'
                                                result['origin'] = origin
                                                results[priori_idx + 1].append(result)
                                else:
                                    if priori_idx == 5 and city in self.populated_cities:
                                        result['value'] = result_value + "-0.1"
                                        origin['segment'] = 'none'
                                        result['origin'] = origin
                                        results[priori_idx + 1].append(result)

            return_result = None
            for priori in range(len(priori_lst) + 1):
                if results[priori]:
                    if priori < 3:
                        return_result = results[priori]
                        break
                    else:
                        high_pop = 0
                        high_idx = 0
                        for idx, a_result in enumerate(results[priori]):
                            if a_result['metadata']['population'] >= high_pop:
                                high_pop = a_result['metadata']['population']
                                high_idx = idx
                        return_result = [results[priori][high_idx]]
                        break
            return return_result

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            print
            ''.join(lines)
            self.log('Exception in create_city_state_country_triple()', _EXCEPTION, url=d[_URL], doc_id=d[_DOCUMENT_ID])
            return None

    @staticmethod
    def print_p(x):
        print
        json.dumps(x, indent=2)

    def filter_results(self, d, config):
        if _KNOWLEDGE_GRAPH not in d:
            return d
        if _STOP_WORD_DICTIONARIES not in config:
            return d

        new_results = list()

        field_name = config[_FIELD_NAME]
        self.load_stop_words(field_name, config[_STOP_WORD_DICTIONARIES])
        if field_name in self.stop_word_dicts:
            if field_name in d[_KNOWLEDGE_GRAPH]:
                results = d[_KNOWLEDGE_GRAPH][field_name]
                for result in results:
                    if result['value'].lower() not in self.stop_word_dicts[field_name]:
                        new_results.append(result)
                if len(new_results) > 0:
                    d[_KNOWLEDGE_GRAPH][field_name] = new_results
                else:
                    kg = d[_KNOWLEDGE_GRAPH]
                    kg.pop(field_name, None)
                    d[_KNOWLEDGE_GRAPH] = kg
        return d

    def add_constant_kg(self, d, config):
        if _KNOWLEDGE_GRAPH not in d:
            return d

        if _CONTANTS not in config:
            return d

        results = list()
        constants = config[_CONTANTS]
        if not isinstance(constants, list):
            constants = [constants]

        for constant in constants:
            if not (isinstance(constant, basestring) or isinstance(constant, numbers.Number)):
                raise Exception(
                    'Only literals can be added to knowledge_graph as constants. Failed to add constant: {}'.format(
                        constant))
            results.append(self.pseudo_extraction_results(constant))
        return results

    @staticmethod
    def create_kg_node_extractor(ds, config, doc, parent_doc_id, doc_id=None, url=None):
        """
        :param d: this is the matched part of doc using input_path
        :param config: config, field_name and segment_name
        :param doc: the input doc, need to add a field called nested_docs
        :param parent_doc_id: doc id of the doc
        :param doc_id: doc_id of the resulting nested doc
        :param url: optional, same as url of the doc
        :return: doc_id of the newly created CDR doc. Since its passed by reference, doc will get updated
                 Or not. who knows
        """
        if _SEGMENT_NAME not in config:
            raise KeyError('{} not found in the config for method: {}'.format(_SEGMENT_NAME,
                                                                              _CREATE_KG_NODE_EXTRACTOR))
        if _DISABLE_DEFAULT_EXT in config and \
                config[_DISABLE_DEFAULT_EXT] != _NO and \
                config[_DISABLE_DEFAULT_EXT] != _YES:
            raise KeyError('{} not acceptable for {} in the config for method: {}'.format(config[_DISABLE_DEFAULT_EXT],
                                                                                          _DISABLE_DEFAULT_EXT,
                                                                                          _CREATE_KG_NODE_EXTRACTOR))
        disable_default_ext = config[_DISABLE_DEFAULT_EXT] if _DISABLE_DEFAULT_EXT in config else _YES

        segment_name = config[_SEGMENT_NAME]

        dataset_id = config.get("dataset_identifier")

        if doc:
            if 'nested_docs' not in doc:
                doc['nested_docs'] = list()

        if not isinstance(ds, list):
            ds = [ds]

        extractions = list()
        class_type = None
        parent_field = _PARENT_DOC_ID
        html_field = None
        if _HTML in config:
            html_field = config[_HTML]
        if '@type' in config:
            class_type = config['@type']
        if 'parent_field' in config:
            parent_field = config['parent_field']
        for d in ds:
            timestamp_created = str(datetime.datetime.now().isoformat())

            result = dict()
            result['@timestamp_created'] = timestamp_created

            result[parent_field] = parent_doc_id
            result[_CREATED_BY] = 'etk'
            if url:
                result[_URL] = url

            result[_CONTENT_EXTRACTION] = dict()
            result[_DISABLE_DEFAULT_EXT] = disable_default_ext

            raw_content = None

            if html_field is not None:
                try:
                    raw_content = d[html_field]
                except:
                    raise KeyError(
                        '{} not found in the document for method: {}'.format(html_field, _CREATE_KG_NODE_EXTRACTOR))
            elif 'html' in d:
                raw_content = d['html']
            elif _TEXT in d:
                raw_content = '<html><body>{}</body></html>'.format(d[_TEXT])
            else:
                raw_content = '<pre><code>{}</code></pre>'.format(json.dumps(d))

            if not doc_id:
                if isinstance(d, basestring) or isinstance(d, numbers.Number):
                    if isinstance(d, numbers.Number):
                        d = str(d)
                    doc_id = hashlib.sha256('{}{}'.format(d, timestamp_created)).hexdigest().upper()
                elif isinstance(d, dict):
                    if _DOC_ID in d and d[_DOC_ID] and isinstance(d[_DOC_ID], basestring):
                        doc_id = d[_DOC_ID]
                    else:
                        doc_id = hashlib.sha256('{}{}'.format(json.dumps(d), timestamp_created)).hexdigest().upper()
                    if '@type' in d:
                        class_type = d['@type']
                else:
                    raise ValueError('cannot process a list of lists: {}, in the method: {}', d,
                                     _CREATE_KG_NODE_EXTRACTOR)

            result[_DOCUMENT_ID] = doc_id
            if raw_content:
                result[_RAW_CONTENT] = raw_content
            result['doc_id'] = doc_id
            if dataset_id:
                result["dataset_identifier"] = dataset_id

            if class_type:
                result['@type'] = class_type

            result[_CONTENT_EXTRACTION][segment_name] = d

            doc['nested_docs'].append(result)
            extractions.append({'value': doc_id, 'key': doc_id, 'metadata': {'timestamp_created': timestamp_created}})
            doc_id = None
        return extractions
