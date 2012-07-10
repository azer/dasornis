<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:with-param name="format">a. </xsl:with-param>
<xsl:template match="/">
<ul>
<xsl:apply-templates />
</ul>
</xsl:template>
	
<xsl:template match="song">
<li><xsl:apply-templates select="title" /></li>
</xsl:template>
	
<xsl:template match="title">
<xsl:value-of select="." />
</xsl:template>

</xsl:stylesheet>