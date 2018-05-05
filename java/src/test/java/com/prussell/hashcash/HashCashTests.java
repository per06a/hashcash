package com.prussell.hashcash;

import static org.assertj.core.api.Assertions.assertThat;
import java.security.DigestException;
import java.security.NoSuchAlgorithmException;

import org.junit.Test;

public class HashCashTests {

	private final String resourceStr = "0xdeadbeef";
	private final int numBits = 15;

	@Test
	public void test_generate() throws NoSuchAlgorithmException, DigestException {
		String stamp = HashCash.generate(numBits, resourceStr);
		assertThat(HashCash.validate(numBits, stamp)).isTrue();
	}

	@Test
	public void test_validate() throws Exception, DigestException {
		/*
		 * Valid stamps from http://www.hashcash.org/stamps/
		 */
		assertThat(HashCash.isValid("1:48:110416:etienne@cri.fr:::000A2F00000063BF012")).isTrue();
		assertThat(HashCash.isValid("1:44:070217:foo::xSi0bPjoswUh6h1Y:TMNI7")).isTrue();
		assertThat(HashCash.isValid(
				"1:42:060922:When I think of all the good times that I've wasted ...::UXkz/DsCCgfvBVtH:00000EF7+j"));
		assertThat(HashCash.isValid(
				"1:41:060704:president@whitehouse.gov::XxcHzSfxDZ38cwRu:000000000000000000000000000000000000m2EDd"));
		assertThat(HashCash.isValid("1:40:051222:foo@bar.org::Cu2iqc4SmotZ7MRR:0000214c3J"));

	}

}
