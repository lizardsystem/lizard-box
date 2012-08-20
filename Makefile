all:

	echo "note: if this fails at lines starting with \"&\" and \"@\" characters, update less to the latest version:"
	echo "      # npm install less"
	# lessc lizard_box/static/lizard_box/lizard_box.less lizard_box/static/lizard_box/lizard_box.css
	coffee -c lizard_box/static/lizard_box/lizard_box.coffee
