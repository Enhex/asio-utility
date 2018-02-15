from conans import ConanFile, tools
import os


class HighlevelasioConan(ConanFile):
	name = "high_level_asio"
	version = "master"
	description = "High level functionality for Asio library"
	no_copy_source = True
	exports_sources = "include/*"
	options = {
		"asio_standalone": [True, False]
	}
	default_options = "asio_standalone=True"

	def requirements(self):
		if self.options.asio_standalone:
			self.requires("asio/master@enhex/stable")
		else:
			self.requires("boost_asio/1.66.0@bincrafters/stable")
	
	def package(self):
		self.copy("*.h")

	def package_id(self):
		self.info.header_only()