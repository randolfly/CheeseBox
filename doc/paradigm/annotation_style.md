## Annotation style

- python 注释

    采用[google](https://google.github.io/styleguide/pyguide.html#381-docstrings)格式，足够轻量而且内容丰富易读，下面是几个例子

    **Module Doc:**
    ```python
    """A one line summary of the module or program, terminated by a period.

    Leave one blank line.  The rest of this docstring should contain an
    overall description of the module or program.  Optionally, it may also
    contain a brief description of exported classes and functions and/or usage
    examples.

    Typical usage example:

    foo = ClassFoo()
    bar = foo.FunctionBar()
    """
    ```

    **Function/Method Doc:**

    遵循的主要原则:

    A function must have a docstring, unless it meets all of the following criteria:

    - not externally visible
    - very short
    - obvious

    注释范式：
    ```python
    def fetch_smalltable_rows(table_handle: smalltable.Table,
                            keys: Sequence[Union[bytes, str]],
                            require_all_keys: bool = False,
    ) -> Mapping[bytes, Tuple[str]]:
        """Fetches rows from a Smalltable.

        Retrieves rows pertaining to the given keys from the Table instance
        represented by table_handle.  String keys will be UTF-8 encoded.

        Args:
            table_handle: An open smalltable.Table instance.
            keys: A sequence of strings representing the key of each table
            row to fetch.  String keys will be UTF-8 encoded.
            require_all_keys: Optional; If require_all_keys is True only
            rows with values set for all keys will be returned.

        Returns:
            A dict mapping keys to the corresponding table row data
            fetched. Each row is represented as a tuple of strings. For
            example:

            {b'Serak': ('Rigel VII', 'Preparer'),
            b'Zim': ('Irk', 'Invader'),
            b'Lrrr': ('Omicron Persei 8', 'Emperor')}

            Returned keys are always bytes.  If a key from the keys argument is
            missing from the dictionary, then that row was not found in the
            table (and require_all_keys must have been False).

        Raises:
            IOError: An error occurred accessing the smalltable.
        """
    ```

    **Class Doc**

    类必须有注释!

    ```python
    class SampleClass:
        """Summary of class here.

        Longer class information....
        Longer class information....

        Attributes:
            likes_spam: A boolean indicating if we like SPAM or not.
            eggs: An integer count of the eggs we have laid.
        """

        def __init__(self, likes_spam=False):
            """Inits SampleClass with blah."""
            self.likes_spam = likes_spam
            self.eggs = 0

        def public_method(self):
            """Performs operation blah."""
    ```

    其余规范见[google](https://google.github.io/styleguide/pyguide.html#381-docstrings)链接，有需要的可以进一步补充。

