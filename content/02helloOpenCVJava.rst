Hello, OpenCV and Java
#######################

:date: 2018-08-29 16:50
:modified: 2018-10-03 23:40
:tags: java; opencv; dip
:category: digital image processing
:slug: opencv-java
:authors: Andre Fellipe da Silva
:summary: A tutorial to use OpenCV with Java. This post was written to the sound of Hall & Oates' `Big Bam Boom`_. You can listen one of the songs here_.

This tutorial will not teach you how to compile your own OpenCV using the source code. I recommend that you try this at a future date for learning purposes. At this moment, let's try a different approach. I am using Ubuntu 18.04 and this tutorial will only work for distributions of the Linux operating system. You will see why below.

Also, I expect that you have a general knowledge about Java. If you know nothing about it so far, just follow the instructions.

Let's dive in!

Checking if you have Java
=========================

Open the terminal (ctrl + alt + T).

Run the following command to check if you already have Java:

.. code-block:: console

    $ java -version

You are good to go if you see something like this:

.. code-block:: console

    java version "1.8.0_181"
    Java(TM) SE Runtime Environment (build 1.8.0_181-b13)
    Java HotSpot(TM) 64-Bit Server VM (build 25.181-b13, mixed mode)

You may have another version of Oracle's Java or OpenJDK, but this should not be a problem.

If you do not see the message above or something similar, you will need to install Java. If you can see the message, jump to the next section.

Run the following commands to install Oracle's Java 8:

.. code-block:: console

    $ sudo add-apt-repository ppa:webupd8team/java
    $ sudo apt-get update
    $ sudo apt-get install oracle-java8-installer

Run the **java -version** command again to make sure everything is fine.

Download OpenCV
===============

Run the following command to install the OpenCV library:

.. code-block:: console

    $ sudo apt-get install libopencv-dev

That's it.

Creating Our First Program
==========================

Using your favorite text editor, create a file named **HelloOpenCVJava.java**. I am using Vim_, so the command would be:

.. code-block:: console

    $ vim HelloOpenCVJava.java

Now, copy and paste the following code:
  
.. code-block:: java

    import org.opencv.core.Core;

    public class HelloOpenCVJava {

      /** Loading the OpenCV library. */
      static {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
      }

      public static void main(String[] args) {

        /** Printing the OpenCV version. */
        System.out.println("Hello OpenCV " + Core.VERSION + "!");

        /** Printing the Java version. */
        System.out.println("Hello to you too, Java " + System.getProperty("java.version") + "!");
      }

    }

Let's breakdown the **HelloOpenCVJava** application.

The **import** keyword is necessary to load the **Core** class from the OpenCV library.

We use the **NATIVE\_LIBRARY\_NAME** property of the Core class to find the corresponding name of the library and use as parameter to the **loadLibrary** method. In this case, it returns **opencv\_java320**. This will allow us to use the OpenCV library. After that, we print the versions of the library and Java.

Compiling and Running HelloOpenCVJava
=====================================

Your project directory must be looking like this right now:

.. code-block:: console

    .
    |__ HelloOpenCVJava.java

If it is, run the following command to compile HelloOpenCVJava.java:

.. code-block:: console

    $ javac -cp /usr/share/OpenCV/java/opencv-320.jar HelloOpenCVJava.java

Now you should have your bytecode class file **HelloOpenCVJava.class**. Here's how the directory should look like:

.. code-block:: console

    .
    |__ HelloOpenCVJava.class
    |__ HelloOpenCVJava.java

The `-cp flag`_ tells the compiler to set the system property java.class.path, which is a list of directories, JAR files and ZIP files that contain class files. We are using here to indicate that we want to find our **opencv-320.jar**.

We have everything we need to run our application now. We do this with the following command:

.. code-block:: console

    $ java -Djava.library.path=/usr/lib/jni -cp /usr/share/OpenCV/java/opencv-320.jar:. HelloOpenCVJava

**-Djava.library.path** sets the **java.library.path** property (-D is a flag to set a system property) to inform the JVM where it can locate native libraries. This property is part of the system environment used by Java, in order to find and load native libraries used by an application.

This should be your output:

.. code-block:: console

    Hello OpenCV 3.2.0!
    Hello to you too, Java 1.8.0_181!

The second line may change depending on your version of Java.

We did it! Well, I did it. I hope that you can replicate this in your machine.

To finish, I would like to point out that in the `OpenCV Java Tutorials Documentation`_ there's a pretty neat tutorial on how to use OpenCV in an IDE like Eclipse_, if you prefer to work in such fashion.

In the next chapter of this journey, we will play a little with Mat objects and some images. Stay tuned!

.. _`Big Bam Boom`: https://en.wikipedia.org/wiki/Big_Bam_Boom
.. _here: https://www.youtube.com/watch?v=s_8KR-n2fBQ
.. _Vim: https://en.wikipedia.org/wiki/Vim_(text_editor)
.. _`-cp flag`: https://docs.oracle.com/javase/8/docs/technotes/tools/windows/findingclasses.html#BABBFCIJ
.. _`OpenCV Java Tutorials Documentation`: https://opencv-java-tutorials.readthedocs.io/en/latest/01-installing-opencv-for-java.html#set-up-opencv-for-java-in-eclipse
.. _Eclipse: https://www.eclipse.org/
